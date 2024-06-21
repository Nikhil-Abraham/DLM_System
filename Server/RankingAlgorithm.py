import math

class RankingAlgorithm:
    def __init__(self, soc_weight, charge_rate_weight, schedule_weight, k):
        self.alpha = soc_weight
        self.beta = charge_rate_weight
        self.gamma = schedule_weight
        self.k = k

    def calculate_priority(self, vehicle, max_charge_rate, current_time):
        soc_score = vehicle.soc/vehicle.desired_soc
        charge_rate_score = vehicle.max_charging_rate/max_charge_rate
        time_to_departure = (vehicle.scheduled_time - current_time).total_seconds()
        time_score = time_score = 1.0 / (1.0 + self.k * time_to_departure)

        priority = self.alpha * soc_score + self.beta * charge_rate_score + self.gamma * time_score
        return priority
    