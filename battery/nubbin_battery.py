from .battery import Battery


class NubbinBattery(Battery):
    def __init__(self, current_date, last_service_date):
        super().__init__(current_date, last_service_date)

    def needs_service(self, service_threshold):
            years_difference = self.current_date.year() - self.last_service_date.year()
            return years_difference >= service_threshold

