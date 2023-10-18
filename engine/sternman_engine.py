from engine.engine import Engine



class SternmanEngine(Engine):
    def __init__(self, last_service_mileage, warning_light_is_on):
        self.warning_light_is_on = warning_light_is_on
        super().__init__(last_service_mileage)
        self.last_service_mileage = last_service_mileage
        

    def needs_service(self):
        return self.warning_light_is_on
    
    