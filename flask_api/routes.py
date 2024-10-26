from flask import Blueprint, request, jsonify, render_template
from models import OcrResult, RagQuery, Alert
from extensions import db
import os
import sys

from services.ocr.mediatotxt import main as process_media
from services.rag.inference_rag_model import main as process_rag_queries

api_blueprint = Blueprint('api', __name__)

@api_blueprint.route('/')
def index():
    return render_template('index.html')

@api_blueprint.route('/map')
def map():
    return render_template('map.html')

@api_blueprint.route('/ocr/upload', methods=['POST'])
def upload_ocr():
    data = request.get_json()
    filename = data.get('filename')

    if not filename:
        return jsonify({"error": "Filename is required"}), 400

    # Call the media processing function from mediatotxt
    combined_output_file = 'flask_api/services/ocr/final_combined_output.txt'
    
    # Run the media processing which should create the combined output
    process_media()

    # Read the combined output
    if not os.path.exists(combined_output_file):
        return jsonify({"error": "Combined output file not found"}), 500

    with open(combined_output_file, 'r') as f:
        extracted_text = f.read()

    # Save OCR result to the database
    result = OcrResult(filename=filename, extracted_text=extracted_text)
    db.session.add(result)
    db.session.commit()

    return jsonify({
        "message": "OCR result saved",
        "id": result.id,
        "filename": result.filename,
        "extracted_text": extracted_text  # Return the extracted text
    }), 201

# Retrieve OCR Results
@api_blueprint.route('/ocr/results', methods=['GET'])
def get_ocr_results():
    results = OcrResult.query.all()
    result_list = [{"id": r.id, "filename": r.filename, "extracted_text": r.extracted_text} for r in results]
    
    if not result_list:
        return jsonify({"message": "No OCR results found"}), 404

    return jsonify(result_list), 200

#  RAG Query Route
@api_blueprint.route('/rag/query', methods=['POST'])
def query_rag():
    data = request.get_json()
    query_text = data.get('query')

    if not query_text:
        return jsonify({"error": "Query text is required"}), 400

    # Create a temporary text file to hold the query
    query_file_path = "flask_api/services/rag/temp_query.txt"
    with open(query_file_path, 'w') as f:
        f.write(query_text)

    # Call the RAG inference function
    process_rag_queries()  # Ensure this function processes the queries as required

    # Read the results from the RAG output file
    output_file_path = "flask_api/services/rag/extracted.txt"
    if not os.path.exists(output_file_path):
        return jsonify({"error": "RAG output file not found"}), 500

    with open(output_file_path, 'r') as f:
        response = f.read()

    # Save RAG query to the database
    query = RagQuery(query_text=query_text, response=response)
    db.session.add(query)
    db.session.commit()

    return jsonify({
        "message": "RAG query saved",
        "id": query.id,
        "query_text": query.query_text,
        "response": query.response
    }), 201

# Retrieve RAG Queries
@api_blueprint.route('/rag/queries', methods=['GET'])
def get_rag_queries():
    queries = RagQuery.query.all()
    query_list = [{"id": q.id, "query_text": q.query_text, "response": q.response} for q in queries]

    if not query_list:
        return jsonify({"message": "No RAG queries found"}), 404

    return jsonify(query_list), 200

# Retrieve Alerts
@api_blueprint.route('/alerts', methods=['GET'])
def get_alerts():
    alerts = Alert.query.all()
    if not alerts:
        return jsonify({"message": "No alerts found"}), 404

    result = [{"id": alert.id, "coordinates": alert.coordinates, 
               "speed": alert.speed, "issue": alert.issue, 
               "red_alert": alert.red_alert} for alert in alerts]

    return jsonify(result), 200