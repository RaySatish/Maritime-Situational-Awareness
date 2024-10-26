import re
import json
from datasets import Dataset, DatasetDict
from transformers import RagTokenizer, RagRetriever, RagSequenceForGeneration, Trainer, TrainingArguments

# Function to parse the markdown file
def parse_markdown_file(md_file_path):
    coordinates = []
    speeds = []
    froms = []
    tos = []
    issues = []
    red_alerts = []
    known_or_not = []

    # Reading the markdown file
    with open(md_file_path, 'r') as file:
        lines = file.readlines()
    
    coordinate_pattern = r'Coordinates:\s*(\d+\.\d+\s*[NS],\s*\d+\.\d+\s*[EW])'
    speed_pattern = r'Speed:\s*(\d+\s*knots)'
    from_pattern = r'From:\s*(.*)'
    to_pattern = r'To:\s*(.*)'
    issue_pattern = r'Issue:\s*(.*)'
    red_alert_pattern = r'Red Alert:\s*(.*)'
    known_or_not_pattern = r'Known or not:\s*(.*)'

    for line in lines:
        # Extract coordinates
        coordinate_match = re.search(coordinate_pattern, line)
        if coordinate_match:
            coordinates.append(coordinate_match.group(1))
        
        # Extract speed
        speed_match = re.search(speed_pattern, line)
        if speed_match:
            speeds.append(speed_match.group(1))
        
        # Extract from
        from_match = re.search(from_pattern, line)
        if from_match:
            froms.append(from_match.group(1))
        
        # Extract to
        to_match = re.search(to_pattern, line)
        if to_match:
            tos.append(to_match.group(1))
        
        # Extract issues/sightings
        issue_match = re.search(issue_pattern, line)
        if issue_match:
            issues.append(issue_match.group(1))
        
        # Extract red alert
        red_alert_match = re.search(red_alert_pattern, line)
        if red_alert_match:
            red_alerts.append(red_alert_match.group(1))
        
        # Extract known or not
        known_or_not_match = re.search(known_or_not_pattern, line)
        if known_or_not_match:
            known_or_not.append(known_or_not_match.group(1))

    return {
        "coordinates": coordinates,
        "speeds": speeds,
        "froms": froms,
        "tos": tos,
        "issues": issues,
        "red_alerts": red_alerts,
        "known_or_not": known_or_not
    }

# Prepare dataset for RAG model
def prepare_rag_dataset(data_dict):
    # Ensure all lists have the same length
    min_length = min(
        len(data_dict["coordinates"]),
        len(data_dict["speeds"]),
        len(data_dict["froms"]),
        len(data_dict["tos"]),
        len(data_dict["issues"]),
        len(data_dict["red_alerts"]),
        len(data_dict["known_or_not"])
    )
    for key in data_dict:
        data_dict[key] = data_dict[key][:min_length]

    dataset_dict = {
        "coordinates": data_dict["coordinates"],
        "speeds": data_dict["speeds"],
        "froms": data_dict["froms"],
        "tos": data_dict["tos"],
        "issues": data_dict["issues"],
        "red_alerts": data_dict["red_alerts"],
        "known_or_not": data_dict["known_or_not"]
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

# Main function to run the training pipeline
def main():
    # Load and parse the markdown file
    md_file_path = "flask_api/services/rag/datasets/Combined_Dataset.md"
    parsed_data = parse_markdown_file(md_file_path)

    # Prepare dataset for the RAG model
    rag_dataset = prepare_rag_dataset(parsed_data)

    # Fine-tune the RAG model on this dataset
    trained_rag_model, tokenizer = fine_tune_rag_model(rag_dataset)

    # Save the trained model and tokenizer
    trained_rag_model.save_pretrained("flask_api/services/rag/trained_model")
    tokenizer.save_pretrained("flask_api/services/rag/trained_model")

if __name__ == "__main__":
    main()