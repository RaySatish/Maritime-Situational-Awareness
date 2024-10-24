from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from geoalchemy2 import Geometry
from flask_socketio import SocketIO
from datetime import datetime
from sqlalchemy import func

# Initialize Flask app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://satishpremanand:22miy0055@localhost/maritime_data'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
socketio = SocketIO(app)

# Database model
class MaritimeContact(db.Model):
    __tablename__ = 'maritime_contacts'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    issue = db.Column(db.String)
    geom = db.Column(Geometry(geometry_type='POINT', srid=4326))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

# Initialize the database tables
def initialize_database():
    with app.app_context():
        db.create_all()

# Route for adding new data
@app.route('/add_contact', methods=['POST'])
def add_contact():
    data = request.json
    name = data['name']
    latitude = data['latitude']
    longitude = data['longitude']
    issue = data.get('issue', 'No issue reported')

    # Store the data in the database
    new_contact = MaritimeContact(
        name=name,
        latitude=latitude,
        longitude=longitude,
        issue=issue,
        geom=f'POINT({longitude} {latitude})'
    )
    db.session.add(new_contact)
    db.session.commit()

    # Process data for threats (example rule: restricted area detection)
    check_for_threat(new_contact)

    return jsonify({'message': 'Contact added successfully'}), 201

# Threat detection and alerts
def check_for_threat(contact):
    # Example: Check if the contact is within a restricted area (e.g., within a certain radius)
    restricted_lat, restricted_lon = 20.0, 70.0  # Example restricted point
    radius = 100  # 100 kilometers

    # Haversine formula to calculate the distance between two points (in kilometers)
    query = db.session.query(
        func.ST_DistanceSphere(
            MaritimeContact.geom, 
            func.ST_MakePoint(restricted_lon, restricted_lat)
        ).label('distance')
    ).filter(MaritimeContact.id == contact.id).first()

    if query.distance <= radius * 1000:  # Convert kilometers to meters
        alert_message = f"Threat detected: {contact.name} is in a restricted area!"
        print(alert_message)

        # Send alert to connected WebSocket clients
        socketio.emit('alert', {'message': alert_message})

# WebSocket route for real-time communication
@socketio.on('connect')
def handle_connect():
    print("Client connected")

@socketio.on('disconnect')
def handle_disconnect():
    print("Client disconnected")

# Run the app and ensure the database is initialized
if __name__ == "__main__":
    initialize_database()  # Ensure tables are created before the server starts
    socketio.run(app, debug=True)
