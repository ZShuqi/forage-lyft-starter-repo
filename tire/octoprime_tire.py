from battery.battery import Battery
from utils import add_years_to_date


class OctoprimeTire(Tire):
    def __init__(self, sensors):
        self.sensors = sensors

    def needs_service(self):
        sum = self.sensors[0] + self.sensors[1] + self.sensors[2] + self.sensors[3]
        if sum >= 3:
            return True
        else:
            return False

    # Better:
    # def needs_service(self):
    #    return sum(self.tire_wear) >= 3.0
