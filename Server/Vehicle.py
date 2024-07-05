from datetime import datetime, timedelta

class Vehicle:
    def __init__(self, soc, max_charging_rate, battery_capacity, scheduled_time=None, desired_soc=100):
        self.soc = soc / 100
        self.desired_soc = desired_soc / 100
        self.max_charging_rate = max_charging_rate
        self.battery_capacity = battery_capacity
        self.scheduled_time = self._parse_scheduled_time(scheduled_time)

    def _parse_scheduled_time(self, scheduled_time):
        if scheduled_time is None:
            return datetime.now() + timedelta(hours=6)
        elif isinstance(scheduled_time, str):
            try:
                parsed_time = datetime.strptime(scheduled_time, '%Y-%m-%dT%H:%M:%S')
                if parsed_time < datetime.now():
                    return datetime.now() + timedelta(hours=6)
                return parsed_time
            except ValueError:
                raise ValueError("Incorrect date format. Expected format: 'YYYY-MM-DDTHH:MM:SS'")
        elif isinstance(scheduled_time, datetime):
            if scheduled_time < datetime.now():
                return datetime.now() + timedelta(hours=6)
            return scheduled_time
        else:
            raise TypeError("Scheduled time must be a string or datetime object.")
    
    def update_soc(self, new_soc):
        self.soc = new_soc / 100
        