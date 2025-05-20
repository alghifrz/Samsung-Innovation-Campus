from flask import Blueprint, request, jsonify
from model import generate_challenge

data_routes = Blueprint('data_routes', __name__)

@data_routes.route('/sensor_data', methods=['POST'])
def receive_sensor_data():
    data = request.get_json()
    raw_sensor_data = data['sensor_data']
    
    challenge = generate_challenge(raw_sensor_data)
    
    return jsonify({'challenge': challenge})
