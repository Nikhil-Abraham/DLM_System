from datetime import datetime, timedelta

class Vehicle:
    def __init__(self, soc, max_charging_rate, battery_capacity, scheduled_time=None, desired_soc=100):
        self.soc = soc/100
        self.desired_soc = desired_soc/100
        self.max_charging_rate = max_charging_rate 
        self.battery_capacity = battery_capacity
        self.scheduled_time = scheduled_time if scheduled_time else datetime.now() + timedelta(hours=6)