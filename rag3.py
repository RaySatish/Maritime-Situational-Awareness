import re
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Define function to extract features from Markdown file
def extract_features_from_markdown(markdown_file):
    # Initialize empty lists for features and labels
    features = []
    labels = []

    # Open Markdown file in read mode
    with open(markdown_file, 'r') as f:
        md = f.read()

    # Extract coordinates (latitude and longitude)
    lat_coords = re.findall(r'\[(.*?)\]: (\d+(\.\d+)?),(\d+(\.\d+)?)', md)
    for lat, lon1, lon2 in lat_coords:
        features.append([float(lat), float(lon1), float(lon2)])

    # Extract issues (assuming they are labels)
    issues = re.findall(r'\[Issue #[0-9]+\]', md)
    if len(issues) > 0:
        labels = [issue.split(']')[1].strip() for issue in issues]
    else:
        print("No issues found in the Markdown file")

    return features, labels

# Define function to train RAG model
def train_rag_model(markdown_file):
    # Extract features and labels from Markdown file
    X, y = extract_features_from_markdown(markdown_file)

    # Debug: Print shapes of X and y
    print(f"Features shape: {np.shape(X)}")
    print(f"Labels shape: {np.shape(y)}")

    if len(y) > 0:
        # Split data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        # Initialize and train Gradient Boosting Classifier
        model = GradientBoostingClassifier()
        model.fit(X_train, y_train)

        # Make predictions and evaluate model
        y_pred = model.predict(X_test)
        print(f"Accuracy: {accuracy_score(y_test, y_pred)}")
        print(f"Classification Report:\n{classification_report(y_test, y_pred)}")
        print(f"Confusion Matrix:\n{confusion_matrix(y_test, y_pred)}")

    else:
        print("No labels found in the Markdown file. Cannot train model.")
        return "No model trained."

    return model

# Example usage
markdown_file = 'datasets/Combined_Dataset.md'
rag_model = train_rag_model(markdown_file)