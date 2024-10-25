from flask import Blueprint, request, jsonify
from models import OcrResult, RagQuery, Alert
from extensions import db

api_blueprint = Blueprint('api', __name__)

@api_blueprint.route('/ocr/upload', methods=['POST'])
def upload_ocr():
    data = request.get_json()
    filename = data.get('filename')
    extracted_text = data.get('extracted_text')

    result = OcrResult(filename=filename, extracted_text=extracted_text)
    db.session.add(result)
    db.session.commit()

    return jsonify({"message": "OCR result saved"}), 201

@api_blueprint.route('/rag/query', methods=['POST'])
def query_rag():
    data = request.get_json()
    query_text = data.get('query')

    # Placeholder for RAG model inference
    response = f"Processed response for: {query_text}"

    query = RagQuery(query_text=query_text, response=response)
    db.session.add(query)
    db.session.commit()

    return jsonify({"query": query_text, "response": response}), 200

@api_blueprint.route('/alerts', methods=['GET'])
def get_alerts():
    alerts = Alert.query.all()
    result = [{"id": alert.id, "coordinates": alert.coordinates, "speed": alert.speed,
               "issue": alert.issue, "red_alert": alert.red_alert} for alert in alerts]

    return jsonify(result), 200
