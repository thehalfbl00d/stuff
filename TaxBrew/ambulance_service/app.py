from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, emit
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json

import os
from config.config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
socketio = SocketIO(app)

# Database Models
class Hospital(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

class Ambulance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    vehicle_number = db.Column(db.String(20), unique=True, nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(20), default='available')  # available, busy, maintenance
    hospital_id = db.Column(db.Integer, db.ForeignKey('hospital.id'), nullable=False)

class EmergencyCall(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(20), default='pending')  # pending, assigned, completed
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    ambulance_id = db.Column(db.Integer, db.ForeignKey('ambulance.id'))
    description = db.Column(db.Text)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard.html')
def dashboard():
    return render_template('dashboard.html')

@app.route('/login.html')
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login_post():
    data = request.json
    email = data.get('email')
    password = data.get('password')
    
    hospital = Hospital.query.filter_by(email=email).first()
    
    if hospital and password == 'password123':  # In production, use proper password hashing
        return jsonify({'success': True, 'redirect': '/dashboard.html'})
    
    return jsonify({'success': False, 'message': 'Invalid credentials'}), 401

@app.route('/signup.html')
def signup():
    return render_template('signup.html')

@app.route('/api/emergency', methods=['POST'])
def create_emergency():
    data = request.json
    new_emergency = EmergencyCall(
        latitude=data['latitude'],
        longitude=data['longitude'],
        description=data['description']
    )
    db.session.add(new_emergency)
    db.session.commit()
    
    # Emit socket event to all connected clients
    socketio.emit('new_emergency', {
        'id': new_emergency.id,
        'latitude': new_emergency.latitude,
        'longitude': new_emergency.longitude,
        'description': new_emergency.description
    })
    
    return jsonify({'message': 'Emergency call created', 'id': new_emergency.id}), 201

@app.route('/api/ambulances', methods=['GET'])
def get_ambulances():
    ambulances = Ambulance.query.all()
    return jsonify([{
        'id': a.id,
        'vehicle_number': a.vehicle_number,
        'latitude': a.latitude,
        'longitude': a.longitude,
        'status': a.status
    } for a in ambulances])

@app.route('/api/ambulance/update-location', methods=['POST'])
def update_ambulance_location():
    data = request.json
    ambulance = Ambulance.query.get(data['id'])
    if ambulance:
        ambulance.latitude = data['latitude']
        ambulance.longitude = data['longitude']
        db.session.commit()
        
        # Emit socket event for real-time updates
        socketio.emit('ambulance_moved', {
            'id': ambulance.id,
            'latitude': ambulance.latitude,
            'longitude': ambulance.longitude
        })
        
        return jsonify({'message': 'Location updated'}), 200
    return jsonify({'message': 'Ambulance not found'}), 404

@socketio.on('connect')
def handle_connect():
    print('Client connected')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    socketio.run(app, host='0.0.0.0', port=8080, debug=True)
