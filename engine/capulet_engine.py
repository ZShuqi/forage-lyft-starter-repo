# from abc import ABC

# from car import Car
from engine.engine import Engine

# class CapuletEngine(Car, ABC):

class CapuletEngine(Engine):
    # engine doesn't need last_service_date data
    # def __init__(self, last_service_date, current_mileage, last_service_mileage):
    def __init__(self, current_mileage, last_service_mileage)
        # super().__init__(last_service_date)
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    # def engine_should_be_serviced(self):
    def needs_service(self):
        return self.current_mileage - self.last_service_mileage > 30000
