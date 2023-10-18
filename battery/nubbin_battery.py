from .battery import Battery
from utils import calculate_years_difference


class NubbinBattery(Battery):
    def __init__(self, current_date, last_service_date):
        super().__init__(current_date, last_service_date)

    def needs_service(self):
            years_difference = calculate_years_difference(self.last_service_date)
            return years_difference >= 4

