from tires.tires import Tires

class CarriganTire(Tire):
    def __init__(self, sensors):
        self.sensors = sensors

    def needs_service(self):
        needs_service = self.sensors[0] < 0.9 and self.sensors[1] < 0.9 and self.sensors[2] < 0.9 and self.sensors[3] < 0.9
        if needs_service:
            return True
        else:
            return False

    # alternative:
    # for tire in self.tire_wear:
    #   if tire >= 0.9:
    #       return True
    #   return False
