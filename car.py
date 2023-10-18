import datetime
from engine.engine import Engine
from battery.battery import Battery



class Car(Battery, Engine):
    def __init__(self, current_date, last_service_mileage, current_mileage, mileage_threshold):
        super().__init__(current_date, last_service_mileage, current_mileage, mileage_threshold)