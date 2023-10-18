from .battery import Battery

class SpindlerBattery(Battery):
    def __init__(self, current_date, last_service_date):
        super().__init__(current_date, last_service_date)
    
    def needs_service(self):
        years_difference = self.current_date.year() - self.last_service_date.year()
        return years_difference >= 2