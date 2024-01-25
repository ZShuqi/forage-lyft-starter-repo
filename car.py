# from abc import ABC, abstractmethod
from serviceable import Serviceable

# class Car(ABC):
class Car(Serviceable):
    # def __init__(self, last_service_date):
    # new initiate parameters: engine & battery
    def __init__(self, engine, battery, tires):
        self.engine = engine
        self.battery = battery
        self.tires = tires
        # self.last_service_date = last_service_date

    # @abstractmethod
    def needs_service(self):
        return self.engine.needs_service() or self.battery.needs_service()
