import re
import json
from datasets import Dataset, DatasetDict
from transformers import RagTokenizer, RagRetriever, RagSequenceForGeneration, Trainer, TrainingArguments

# Function to parse the markdown file
def parse_markdown_file(md_file_path):
    coordinates = []
    issues = []

    # Reading the markdown file
    with open(md_file_path, 'r') as file:
        lines = file.readlines()
    
    # Example parsing: Adjust regex based on your markdown format
    coordinate_pattern = r'Coordinates:\s*(\d+\.\d+\s*[NS],\s*\d+\.\d+\s*[EW])'
    issue_pattern = r'Issue:\s*(.*)'

    for line in lines:
        # Extract coordinates
        coordinate_match = re.search(coordinate_pattern, line)
        if coordinate_match:
            coordinates.append(coordinate_match.group(1))
        
        # Extract issues/sightings
        issue_match = re.search(issue_pattern, line)
        if issue_match:
            issues.append(issue_match.group(1))

    return {"coordinates": coordinates, "issues": issues}

# Prepare dataset for RAG model
def prepare_rag_dataset(data_dict):
    dataset_dict = {
        "coordinates": data_dict["coordinates"],
        "issues": data_dict["issues"],
    }
    
    dataset = Dataset.from_dict(dataset_dict)
    return DatasetDict({"train": dataset})

# Load and fine-tune RAG model
def fine_tune_rag_model(dataset):
    tokenizer = RagTokenizer.from_pretrained("facebook/rag-sequence-nq")
    retriever = RagRetriever.from_pretrained("facebook/rag-sequence-nq", index_name="exact", use_dummy_dataset=False)

    # Fine-tune with RAG
    rag_model = RagSequenceForGeneration.from_pretrained("facebook/rag-sequence-nq", retriever=retriever)

    training_args = TrainingArguments(
        output_dir='./results',
        num_train_epochs=3,   # Increase for better results
        per_device_train_batch_size=2,
        save_steps=10_000,
        save_total_limit=2,
        logging_dir='./logs',
    )

    trainer = Trainer(
        model=rag_model,
        args=training_args,
        train_dataset=dataset["train"],
        tokenizer=tokenizer
    )

    trainer.train()
    return rag_model, tokenizer

# Main function to run the pipeline
def main():
    # Load and parse the markdown file
    md_file_path = "/Users/satishpremanand/Documents/GitHub/Maritime-Situational-Awareness/datasets/Combined_Dataset.md"
    parsed_data = parse_markdown_file(md_file_path)

    # Prepare dataset for the RAG model
    rag_dataset = prepare_rag_dataset(parsed_data)

    # Fine-tune the RAG model on this dataset
    trained_rag_model, tokenizer = fine_tune_rag_model(rag_dataset)

    # Test with a sample query (use actual maritime data query here)
    sample_query = "Unidentified vessel spotted near 30.5 N, 50.1 W. What direction is it moving?"
    input_dict = tokenizer.prepare_seq2seq_batch([sample_query], return_tensors="pt")
    generated = trained_rag_model.generate(input_ids=input_dict["input_ids"])

    # Decode and print the result
    result = tokenizer.batch_decode(generated, skip_special_tokens=True)[0]
    print("Generated Response:", result)

if __name__ == "__main__":
    main()