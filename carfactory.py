from car import Car

# from engine.model.calliope import Calliope

class CarFactory(Car, ABC):
    def __init__(self, current_date, last_service_date, current_mileage, last_service_mileage):
        self.last_service_date = last_service_date

    @abstractmethod
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage):
        return new Car()
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage):
        return new Car(last_service_date)
    def create_palindrome(current_date, last_service_date, warning_light_on):
        return new Car(last_service_date)
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage):
        return new Car(last_service_date)
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage):
        return new Car(last_service_date)
