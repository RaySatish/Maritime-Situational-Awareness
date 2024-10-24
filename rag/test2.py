import os
import re
import pandas as pd
import numpy as np
import faiss
import torch
from sentence_transformers import SentenceTransformer
from transformers import RagTokenizer, RagSequenceForGeneration, Trainer, TrainingArguments

# Load and process a single Markdown file
def load_markdown_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()
    return content

# Preprocess content to extract relevant information
def preprocess_content(content):
    # Example: Extracting lines that may contain coordinates or vessel types
    lines = content.split('\n')
    processed_lines = []
    for line in lines:
        # Basic filtering based on content (customize as needed)
        if re.search(r'latitude|longitude|vessel|sighted', line, re.IGNORECASE):
            processed_lines.append(line.strip())
    return processed_lines

# Load data from the specified Markdown file
file_path = 'datasets/Combined_Dataset.md'
markdown_content = load_markdown_file(file_path)

# Process the content
processed_data = preprocess_content(markdown_content)

# Create a DataFrame from the processed data
df = pd.DataFrame({'content': processed_data})

# Set up the embedding model for retrieval
embedding_model = SentenceTransformer('all-MiniLM-L6-v2')

# Generate embeddings for the processed data
embeddings = embedding_model.encode(df['content'].tolist())

# Create a FAISS index for efficient retrieval
index = faiss.IndexFlatL2(embeddings.shape[1])  # L2 distance
index.add(np.array(embeddings).astype('float32'))

# Ensure the data directory exists before writing the index
output_directory = 'data'
os.makedirs(output_directory, exist_ok=True)  # Create the directory if it doesn't exist

# Save the index for later use
faiss.write_index(index, os.path.join(output_directory, 'faiss_index.index'))

# Prepare the RAG model and tokenizer
tokenizer = RagTokenizer.from_pretrained('facebook/rag-sequence-nq')
rag_model = RagSequenceForGeneration.from_pretrained('facebook/rag-sequence-nq')

# Tokenize inputs for training
def tokenize_function(examples):
    return tokenizer(examples, padding='max_length', truncation=True, return_tensors='pt')

# Convert the DataFrame content to a list of strings for tokenization
content_list = df['content'].tolist()

# Tokenize the content for the training dataset
tokenized_data = tokenize_function(content_list)

# Set up training arguments
training_args = TrainingArguments(
    output_dir='./logs',
    evaluation_strategy='epoch',
    per_device_train_batch_size=4,
    num_train_epochs=3,
    save_steps=1000,
    logging_dir='./logs',
    logging_steps=100,
)

# Create a PyTorch Dataset from the tokenized data
class CustomDataset(torch.utils.data.Dataset):
    def __init__(self, encodings):
        self.encodings = encodings

    def __getitem__(self, idx):
        return {key: val[idx] for key, val in self.encodings.items()}

    def __len__(self):
        return len(self.encodings['input_ids'])

train_dataset = CustomDataset(tokenized_data)

# Create a Trainer instance
trainer = Trainer(
    model=rag_model,
    args=training_args,
    train_dataset=train_dataset,
)

# Train the model
trainer.train()

# Save the trained model and tokenizer
rag_model.save_pretrained('models/trained_rag_model')
tokenizer.save_pretrained('models/trained_rag_model')

print("RAG model training complete. Model saved to 'models/trained_rag_model'.")
