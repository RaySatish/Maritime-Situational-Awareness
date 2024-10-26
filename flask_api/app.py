from flask import Flask
from extensions import db, migrate
from routes import api_blueprint
from flask_cors import CORS
import os

# Initialize Flask app
app = Flask(_name_)
CORS(app, resources={r"/": {"origins": ""}})

# Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'postgresql://myuser:mypassword@localhost/mydb')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize extensions
db.init_app(app)
migrate.init_app(app, db)

# Register routes
app.register_blueprint(api_blueprint)

if _name_ == "_main_":
    app.run(host='0.0.0.0', port=5000, debug=True, use_reloader=False)