from extensions import db

class OcrResult(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(100), nullable=False)
    extracted_text = db.Column(db.Text, nullable=False)

class RagQuery(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    query_text = db.Column(db.Text, nullable=False)
    response = db.Column(db.Text, nullable=False)

class Alert(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    coordinates = db.Column(db.String(100), nullable=False)
    speed = db.Column(db.String(50), nullable=False)
    issue = db.Column(db.String(200), nullable=False)
    red_alert = db.Column(db.String(50), nullable=False)