from battery.battery import Battery
from utils import add_years_to_date


class CarriganTire(Tire):
    def __init__(self, sensors):
        self.sensors = sensors

    def needs_service(self):
        needs_service = sensors[0] < 0.9 and sensors[1] < 0.9 and sensors[2] < 0.9 and sensors[3] < 0.9
        if needs_service:
            return True
        else:
            return False
