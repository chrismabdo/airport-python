class Airport:

    MAXIMUM_1 = 3
    def __init__(self):
        self.hangar = []

    def land(self, plane):
        self.full_capacity(plane)

    def take_off(self, plane):
        self.hangar.remove(plane)

    def full_capacity(self, plane):
        if len(self.hangar) == 3:
            return "Hangar Capacity Reached!"
        else:
            self.hangar.append(plane)

