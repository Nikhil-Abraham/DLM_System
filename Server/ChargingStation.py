from datetime import datetime

class ChargingStation: 
    def __init__(self, station_id, max_charge_rate, priority_algorithm):
        self.station_id = station_id
        self.priority_algorithm = priority_algorithm
        self.vehicle_is_connected = False
        self.vehicle = None
        self.max_charge_rate = max_charge_rate
        self.max_feasible_rate = 0
        self.charge_rate = 0
        self.charger_priority = 0
        self.estimated_charging_time = 0

    def connect_vehicle(self, vehicle):
        if not self.vehicle_is_connected:
            self.vehicle = vehicle
            current_time = datetime.now()
            self.charger_priority = self.priority_algorithm.calculate_priority(self.vehicle, self.max_charge_rate, current_time)
            self.vehicle_is_connected = True
            self.max_feasible_rate = min(self.max_charge_rate, self.vehicle.max_charging_rate)
            charging_time = (self.vehicle.desired_soc*vehicle.battery_capacity - self.vehicle.soc*self.vehicle.battery_capacity)/self.max_feasible_rate
            if charging_time < 0:
                charging_time = 0
            self.estimated_charging_time = charging_time
        else:
            raise Exception("Charging station is already occupied")
    
    def disconnect_vehicle(self):
        self.vehicle_is_connected = None
        self.vehicle = None
        self.charger_priority = 0
        self.charge_rate = 0
        self.max_feasible_rate = 0
        self.estimated_charging_time = 0
    
    
    def get_charging_stats(self):
        if self.vehicle_is_connected:
            return {
                "station_id": self.station_id,
                "plant_capacity": self.plant_capacity,
                "vehicle_is_connected": self.vehicle_is_connected,
                "charger_priority": self.charger_priority,
                "max_feasible_rate": self.max_feasible_rate
            }
        return None