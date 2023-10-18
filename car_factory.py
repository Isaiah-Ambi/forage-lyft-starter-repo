from datetime import datetime
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import  WilloughbyEngine



current_date = datetime.today().date()

class CarFactory():
    #def __init__():

    def create_calliope(self, last_service_date, last_service_mileage, current_mileage):
        battery = SpindlerBattery(current_date, last_service_date)
        engine = CapuletEngine(last_service_mileage, current_mileage)
        return engine.needs_service() or battery.needs_service()
        

    def create_glissade(self, last_service_date, last_service_mileage, current_mileage):
        battery = SpindlerBattery(current_date,last_service_date)
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        return engine.needs_service() or battery.needs_service()

    def create_palindrome(self, last_service_date, warning_light_is_on):
        battery = SpindlerBattery(current_date, last_service_date)
        engine = SternmanEngine(warning_light_is_on)
        return engine.needs_service() or battery.needs_service()

    def create_rorschach(self, last_service_date, last_service_mileage, current_mileage):
        battery = NubbinBattery(current_date, last_service_date)
        engine = CapuletEngine(last_service_mileage, current_mileage)
        return engine.needs_service() or battery.needs_service()
    
    def create_thovex(self, last_service_date, last_service_mileage, current_mileage):
        battery = NubbinBattery(current_date, last_service_date)
        engine = CapuletEngine(last_service_mileage, current_mileage)
        return engine.needs_service() or battery.needs_service()


'''def main():
    last_service_date = datetime(2021, 1, 1).date()
    car = CarFactory.create_glissade(last_service_date, 30000, 60000)
    status = car.needs_service()

    print(status)
if __name__ == "__main__":
    main()
'''


