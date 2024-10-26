import os
from transformers import RagTokenizer, RagSequenceForGeneration
try:
    from .train_rag_model import main as train_rag_model
except ImportError:
    from train_rag_model import main as train_rag_model

# Function to process queries from a text file
def process_queries(txt_file_path, rag_model, tokenizer):
    with open(txt_file_path, 'r') as file:
        queries = file.readlines()

    results = []
    for query in queries:
        input_dict = tokenizer.prepare_seq2seq_batch([query.strip()], return_tensors="pt")
        generated = rag_model.generate(input_ids=input_dict["input_ids"])
        result = tokenizer.batch_decode(generated, skip_special_tokens=True)[0]
        results.append(result)
    
    return results

# Main function to run the inference pipeline
def main():
    model_path = "flask_api/services/rag/trained_model"

    # Check if the trained model and tokenizer are already saved on disk
    if os.path.exists(model_path):
        # Load the trained model and tokenizer
        trained_rag_model = RagSequenceForGeneration.from_pretrained(model_path)
        tokenizer = RagTokenizer.from_pretrained(model_path)
    else:
        # Train the model and save it
        trained_rag_model, tokenizer = train_rag_model()
        trained_rag_model.save_pretrained(model_path)
        tokenizer.save_pretrained(model_path)

    # Process queries from the text file
    txt_file_path = "flask_api/services/ocr/final_combined_output.txt"
    results = process_queries(txt_file_path, trained_rag_model, tokenizer)

    # Write the results to a .txt file
    output_file_path = "flask_api/services/rag/extracted.txt"
    with open(output_file_path, 'w') as output_file:
        for result in results:
            output_file.write(f"{result}\n")

if __name__ == "__main__":
    main()