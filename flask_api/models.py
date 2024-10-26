from extensions import db

class OcrResult(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(128), nullable=False)
    extracted_text = db.Column(db.Text, nullable=False)

class RagQuery(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    query_text = db.Column(db.Text, nullable=False)
    response = db.Column(db.Text, nullable=False)

class Alert(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    coordinates = db.Column(db.String(64))
    speed = db.Column(db.String(32))
    issue = db.Column(db.String(256))
    red_alert = db.Column(db.Boolean, default=False)
