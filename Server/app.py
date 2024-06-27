from flask import Flask, jsonify, request
from flask_cors import CORS
from DynaminLoadManager import DynaminLoadManager
from ChargingStation import ChargingStation
from Vehicle import Vehicle
from RankingAlgorithm import RankingAlgorithm
from datetime import datetime, timedelta

app = Flask(__name__)
CORS(app)  # Enable CORS for all origins by default

# Initialize Ranking Algorithm
Algo1 = RankingAlgorithm(0.2, 0.3, 0.5, 1)

# Initialize Dynamic Load Manager
DLM = DynaminLoadManager([], 100, 100, Algo1)

# Home Endpoint
@app.route('/')
def home():
    return jsonify({"message": "Welcome to the EV Charging System"})

# Configure System Endpoint
@app.route('/configure_system', methods=['POST'])
def configure_system():
    data = request.json
    internal_capacity = data.get('internal_capacity')
    battery_capacity = data.get('battery_capacity')

    DLM.update_system_config(internal_capacity, battery_capacity)
    
    return jsonify({"message": "System configuration updated successfully"})

# Update Building Load Endpoint
@app.route('/update_building_load', methods=['POST'])
def update_building_load():
    data = request.json
    new_load = data.get('new_load')

    DLM.update_building_load(new_load)

    return jsonify({"message": "Building load updated successfully"})

# Divert Battery Capacity Endpoint
@app.route('/divert_battery_capacity', methods=['POST'])
def divert_battery_capacity():
    data = request.json
    capacity = data.get('capacity')

    DLM.divert_battery_capacity_to_charging(capacity)

    return jsonify({"message": "Battery capacity diverted successfully"})

@app.route('/add_station', methods=['POST'])
def add_station():
    data = request.json
    station_id = data.get('station_id')
    max_charge_rate = data.get('max_charge_rate')

    # Check if the station with the same ID already exists
    for station in DLM.stations:
        if station.station_id == station_id:
            return jsonify({"error": f"Station {station_id} already exists"}), 400

    # Create a new ChargingStation object
    new_station = ChargingStation(station_id, max_charge_rate, Algo1)

    # Add the new station to the stations list
    if len(DLM.stations) >= 5:
        return jsonify({"error": "Maximum number of stations (5) reached"}), 400

    # Add the station to the Dynamic Load Manager
    DLM.add_station(new_station)

    return jsonify({"message": f"Station {station_id} added successfully"})


# Remove Station Endpoint
@app.route('/remove_station/<station_id>', methods=['DELETE'])
def remove_station(station_id):
    for station in DLM.stations:
        if station.station_id == station_id:
            DLM.remove_station(station_id)
            return jsonify({"message": f"Station {station_id} removed successfully"})

    return jsonify({"error": f"Station {station_id} not found"}), 404

@app.route('/connect_vehicle', methods=['POST'])
def connect_vehicle():
    data = request.json
    station_id = data.get('station_id')
    vehicle_info = data.get('vehicle')

    # Log the incoming data for debugging
    print(f"Received station_id: {station_id}")
    print(f"Received vehicle_info: {vehicle_info}")

    for station in DLM.stations:
        print(f"Checking station: {station.station_id}")
        if station.station_id == station_id:
            try:
                vehicle = Vehicle(**vehicle_info)
                station.connect_vehicle(vehicle)
                DLM.distribute_load()
                return jsonify({"message": f"Vehicle connected to {station_id} successfully"})
            except Exception as e:
                print(f"Error: {str(e)}")
                return jsonify({"error": str(e)}), 400
    print(vars(DLM))

    return jsonify({"error": f"Station {station_id} not found"}), 404


# Disconnect Vehicle Endpoint
@app.route('/disconnect_vehicle/<station_id>', methods=['POST'])
def disconnect_vehicle(station_id):
    for station in DLM.stations:
        if station.station_id == station_id:
            if station.vehicle_is_connected:
                station.disconnect_vehicle()
                DLM.distribute_load()
                return jsonify({"message": f"Vehicle disconnected from {station_id} successfully"})
            else:
                return jsonify({"error": f"No vehicle connected to {station_id}"}), 400

    return jsonify({"error": f"Station {station_id} not found"}), 404

# Get Load Distribution Endpoint
@app.route('/load_distribution', methods=['GET'])
def load_distribution():
    return jsonify(DLM.get_load_distribution())

# Main Function to Run the Application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
