class Airport:
    MAXIMUM_CAPACITY = 3
    def __init__(self, capacity=MAXIMUM_CAPACITY):
        self.capacity = capacity
        self.hangar = []

    def land(self, plane):
        if len(self.hangar) == self.capacity:
          return "Hangar Capacity Reached!"
        else:
          self.hangar.append(plane)

    def take_off(self, plane):
        self.hangar.remove(plane)


    # def full_capacity(self, plane)