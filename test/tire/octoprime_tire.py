from battery.battery import Battery
from utils import add_years_to_date


class OctoprimeTire(Tire):
    def __init__(self, sensors):
        self.sensors = sensors

    def needs_service(self):
        sum = sensors[0] + sensors[1] + sensors[2] + sensors[3]
        if sum >= 3:
            return True
        else:
            return False
