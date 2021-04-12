class Airport:

    
    def __init__(self):
        self.MAXIMUM_CAPACITY = 3
        self.hangar = []

    def land(self, plane):
        if len(self.hangar) == self.MAXIMUM_CAPACITY:
          return "Hangar Capacity Reached!"
        else:
          self.hangar.append(plane)

    def take_off(self, plane):
        self.hangar.remove(plane)

    # def full_capacity(self, plane)