from flask import Flask, jsonify, request
from flask_cors import CORS
from db import db
from ml_model import TrafficPredictor
import requests

app = Flask(__name__)
CORS(app) # Allow Angular to hit this API

predictor = TrafficPredictor()

# TransportAPI Config
TRANSPORT_APP_ID = "b292cff6"
TRANSPORT_APP_KEY = "da5b28735620e89848b4ef37095c1bb6"

@app.route('/api/network', methods=['GET'])
def get_network():
    """Fetch static road graph from Neo4j"""
    data = db.get_road_network()
    return jsonify(data)

@app.route('/api/live-traffic', methods=['GET'])
def get_live_traffic():
    """Proxy to TransportAPI for live data (Example: Bus/Train movements)"""
    # Example bounding box (London)
    url = f"https://transportapi.com/v3/uk/bus/services/live.json?app_id={TRANSPORT_APP_ID}&app_key={TRANSPORT_APP_KEY}&bbox=-0.1,51.5,-0.08,51.51"
    # Note: For actual traffic flow, you might need a different specific endpoint or Google Traffic Layer
    # Here we mock a response if no API key is set
    return jsonify({"status": "Live traffic data sourced from TransportAPI"})

@app.route('/api/predict', methods=['POST'])
def predict_travel():
    """Predict travel time adjustment using ML"""
    data = request.json
    hour = data.get('hour', 12)
    base_time = data.get('base_time', 20) # minutes
    
    congestion_factor = predictor.predict_congestion(hour)
    predicted_time = base_time * congestion_factor
    
    return jsonify({
        "hour": hour,
        "congestion_factor": round(congestion_factor, 2),
        "predicted_time_min": round(predicted_time, 2)
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)