import unittest
from datetime import datetime


from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import  WilloughbyEngine
from car_factory import CarFactory  # Assuming your CarFactory class is in a file named car_factory.py
from utils import calculate_years_difference


class TestCarFactory(unittest.TestCase):
    def setUp(self):
        self.current_date = datetime.today().date()

    def test_spindler(self):
        last_service_date = datetime(2020, 10, 1).date()
        battery = SpindlerBattery(self.current_date, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_nubbin(self):
        last_service_date = datetime(2017, 10, 1).date()
        battery = NubbinBattery(self.current_date, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_capulet(self):
        last_service_date = datetime(2020, 10, 1).date()
        engine = CapuletEngine(0, 30001)
        #battery = NubbinBattery(self.current_date, last_service_date)
        self.assertTrue(engine.needs_service())
    
    def test_sternman(self):
        last_service_date = datetime(2020, 10, 1).date()
        engine = SternmanEngine(30001, True )
        #battery = NubbinBattery(self.current_date, last_service_date)
        self.assertTrue(engine.needs_service())
    
    def test_willoughby(self):
        last_service_date = datetime(2020, 10, 1).date()
        engine = WilloughbyEngine(0, 60001)
        #battery = NubbinBattery(self.current_date, last_service_date)
        self.assertTrue(engine.needs_service())


if __name__ == "__main__":
    unittest.main()
