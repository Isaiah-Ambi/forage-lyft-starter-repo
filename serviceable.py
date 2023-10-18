from abc import ABC, absctractmethod


class Serviceable(ABC):
    @absctractmethod
    def needs_service(self):
        pass