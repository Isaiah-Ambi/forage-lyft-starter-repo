from tires import Tires


class OctoprimeTires(Tires):
    def __init__(self, tire_wear):
        super().__init__()
        self.tire_wear = tire_wear

    def needs_service(self):
        wear = sum(self.tire_wear)
        return wear >= 3 
