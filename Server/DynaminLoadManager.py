from RankingAlgorithm import RankingAlgorithm
from datetime import datetime
import json

class DynaminLoadManager:
    def __init__(self, stations, internal_capacity, battery_capacity, priority_algorithm):
        self.stations = stations
        self.priority_algorithm = priority_algorithm
        self.internal_capacity = internal_capacity
        self.available_capacity = internal_capacity
        self.battery_capacity = battery_capacity
        self.battery_capacity_diverted = 0
        self.battery_capacity_available = battery_capacity
        self.building_load = 0
        self.capacity_utilization = 0
    
    def refresh_station_priority(self):
        for station in self.stations:
            if station.vehicle_is_connected:
                current_time = datetime.now()
                station.charger_priority =self.priority_algorithm.calculate_priority(station.vehicle, station.max_charge_rate, current_time)
    
    def get_total_required_capacity(self):
        total_required_capacity = 0
        for station in self.stations:
            total_required_capacity += station.max_feasible_rate
        return total_required_capacity

    def add_station(self, station):
        print("Adding Station")
        self.stations.append(station)
        self.distribute_load()
        print(vars(self))

    def remove_station(self, station_id):
        for station in self.stations:
            if station.station_id == station_id:
                self.stations.remove(station)
                self.distribute_load()
                return
        return

    def update_building_load(self, new_load):
        self.building_load = new_load
        self.distribute_load()

    def update_system_config(self, internal_capacity, battery_capacity):
        self.internal_capacity = internal_capacity
        self.battery_capacity = battery_capacity
        self.battery_capacity_available = battery_capacity - self.battery_capacity_diverted
        self.distribute_load()

    def divert_battery_capacity_to_charging(self, capacity):
        if capacity < self.battery_capacity:
            self.battery_capacity_diverted = capacity
            self.battery_capacity_available = self.battery_capacity - capacity
            self.distribute_load()
    
    def update_available_capacity(self):
        self.available_capacity = self.internal_capacity + self.battery_capacity_diverted - self.building_load
    
    def update_vehicle_soc(self, station_id, new_soc):
        for station in self.stations:
            if station.station_id == station_id:
                station.vehicle.soc = new_soc
                station.estimated_charging_time = (station.vehicle.desired_soc*station.vehicle.battery_capacity - station.vehicle.soc*station.vehicle.battery_capacity)/station.max_feasible_rate
                if station.estimated_charging_time < 0:
                    station.estimated_charging_time = 0
                self.distribute_load()
                return
        return

    
    def distribute_load(self):
            self.refresh_station_priority()
            sorted_stations = sorted(self.stations, key=lambda x: x.charger_priority, reverse=True)
            required_capacity = self.get_total_required_capacity()
            
            self.update_available_capacity()

            if required_capacity <= self.available_capacity:
                for station in sorted_stations:
                    station.charge_rate = station.max_feasible_rate
                self.capacity_utilization = sum(station.charge_rate for station in self.stations if station.vehicle_is_connected)
            else:
                total_priority = sum(station.charger_priority for station in sorted_stations)
                remaining_capacity = self.available_capacity

                for station in sorted_stations:
                    if remaining_capacity <= 0:
                        station.charge_rate = 0
                        continue

                    allocation_ratio = station.charger_priority / total_priority
                    proposed_charge_rate = allocation_ratio * self.available_capacity

                    if proposed_charge_rate <= station.max_feasible_rate:
                        station.charge_rate = proposed_charge_rate
                        remaining_capacity -= proposed_charge_rate
                    else:
                        station.charge_rate = station.max_feasible_rate
                        remaining_capacity -= station.max_feasible_rate

                # Redistribute any remaining capacity if initial allocation left some capacity
                if remaining_capacity > 0:
                    remaining_stations = [station for station in sorted_stations if station.charge_rate < station.max_feasible_rate]
                    num_remaining_stations = len(remaining_stations)

                    if num_remaining_stations > 0:
                        additional_capacity_per_station = remaining_capacity / num_remaining_stations

                        for station in remaining_stations:
                            max_feasible_rate = min(station.max_feasible_rate, station.vehicle.max_charging_rate)
                            if station.charge_rate < max_feasible_rate:
                                additional_capacity = min(max_feasible_rate - station.charge_rate, additional_capacity_per_station)
                                station.charge_rate += additional_capacity
                                remaining_capacity -= additional_capacity

                self.capacity_utilization = sum(station.charge_rate for station in self.stations if station.vehicle_is_connected)


    def get_load_distribution(self):
        print("Load Distribution")
        print(vars(self))
        distribution = {
            "System": {
                "internal_capacity": self.internal_capacity,
                "battery_capacity": self.battery_capacity,
                "battery_capacity_diverted": self.battery_capacity_diverted,
                "battery_capacity_available": self.battery_capacity_available,
                "building_load": self.building_load,
                "available_capacity": self.available_capacity,
                "capacity_utilization": self.capacity_utilization,
            }
        }
        stations = []
        for station in self.stations:
            stations.append({
                "station_id": station.station_id,
                "max_feasible_rate": station.max_feasible_rate,
                "charge_rate": station.charge_rate,
                "charger_priority": station.charger_priority,
                # if vehicle is connected, include vehicle stats else leave vehicle object empty
                "vehicle": {
                    "vehicle_soc": station.vehicle.soc,
                    "vehicle_battery_capacity": station.vehicle.battery_capacity,
                    "vehicle_max_charging_rate": station.vehicle.max_charging_rate,
                    "vehicle_scheduled_time": (station.vehicle.scheduled_time - datetime.now()).total_seconds()/3600,
                    "vehicle_desired_soc": station.vehicle.desired_soc,
                    "estimated_charging_time": station.estimated_charging_time
                    } if station.vehicle_is_connected else {},

            })
        distribution["stations"] = stations
        print(json.dumps(distribution, indent=2))
        return distribution
