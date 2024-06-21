from DynaminLoadManager import DynaminLoadManager
from ChargingStation import ChargingStation
from Vehicle import Vehicle
from RankingAlgorithm import RankingAlgorithm
from datetime import datetime, timedelta
import time


Algo1 = RankingAlgorithm(0.2, 0.3, 0.5, 1)


EV1 = Vehicle(soc=70, max_charging_rate=25, battery_capacity=100, desired_soc=80, scheduled_time=datetime.now() + timedelta(hours=2))
EV2 = Vehicle(soc=50, max_charging_rate=35, battery_capacity=100, desired_soc=60, scheduled_time=datetime.now() + timedelta(hours=3))
EV3 = Vehicle(soc=90, max_charging_rate=35, battery_capacity=100, desired_soc=100, scheduled_time=datetime.now() + timedelta(hours=1))
EV4 = Vehicle(soc=70, max_charging_rate=25, battery_capacity=100)
EV5 = Vehicle(soc=20, max_charging_rate=25, battery_capacity=100)
EV6 = Vehicle(soc=30, max_charging_rate=25, battery_capacity=100)
EV7 = Vehicle(soc=50, max_charging_rate=25, battery_capacity=200)


S1 = ChargingStation("S1", 30, Algo1)
S2 = ChargingStation("S2", 30, Algo1)
S3 = ChargingStation("S3", 20, Algo1)
S4 = ChargingStation("S4", 30, Algo1)
S5 = ChargingStation("S5", 30, Algo1)

stations = [S1, S2, S3, S4, S5]

DLM = DynaminLoadManager(stations, 100, 100, Algo1)

DLM.get_load_distribution()
print('\n------------------------------------\n')

#time.sleep(6)

print('EV1 is connecting to S1')
S1.connect_vehicle(EV1)
DLM.distribute_load()
DLM.get_load_distribution()
print('\n------------------------------------\n')

#time.sleep(6)

print('EV2 is connecting to S2')
S2.connect_vehicle(EV2)
DLM.distribute_load()
DLM.get_load_distribution()
print('\n------------------------------------\n')

#time.sleep(6)

print('EV3 is connecting to S3')
S3.connect_vehicle(EV3)
DLM.distribute_load()
DLM.get_load_distribution()
print('\n------------------------------------\n')

#time.sleep(6)

print('EV4 is connecting to S4')
S4.connect_vehicle(EV4)
DLM.distribute_load()
DLM.get_load_distribution()
print('\n------------------------------------\n')

#time.sleep(6)

print('EV5 is connecting to S5')
S5.connect_vehicle(EV5)
DLM.distribute_load()
DLM.get_load_distribution()
print('\n------------------------------------\n')

#time.sleep(6)

print('Increasing the building load to 50')
DLM.update_building_load(50)
DLM.get_load_distribution()
print('\n------------------------------------\n')

#time.sleep(6)

print('Diverting 20 capacity to charging')
DLM.divert_battery_capacity_to_charging(20)
DLM.get_load_distribution()
print('\n------------------------------------\n')

print('EV4 is disconnecting from S4')
S4.disconnect_vehicle()
DLM.distribute_load()
DLM.get_load_distribution()
print('\n------------------------------------\n')

#time.sleep(6)

print('EV3 is disconnecting from S3')
S3.disconnect_vehicle()
DLM.distribute_load()
DLM.get_load_distribution()
print('\n------------------------------------\n')

#time.sleep(6)

print('EV6 is connecting t0 S4')
S4.connect_vehicle(EV6)
DLM.distribute_load()
DLM.get_load_distribution()
print('\n------------------------------------\n')

#time.sleep(6)

print('EV7 is connecting to S3')
S3.connect_vehicle(EV7)
DLM.distribute_load()
DLM.get_load_distribution()
print('\n------------------------------------\n')