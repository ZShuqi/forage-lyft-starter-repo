# from abc import ABC

# from car import Car
from engine.engine import Engine

class SternmanEngine(Car, ABC):
    # def __init__(self, last_service_date, warning_light_is_on):
    def __init__(self, warning_light_is_on):
        # super().__init__(last_service_date)
        self.warning_light_is_on = warning_light_is_on

    # def engine_should_be_serviced(self):
    def needs_service(self):
        if self.warning_light_is_on:
            return True
        else:
            return False
