import random

class Airport:
    MAXIMUM_CAPACITY = 3
    def __init__(self, capacity=MAXIMUM_CAPACITY):
        self.capacity = capacity
        self.hangar = []

    def land(self, plane):
        if self.full_capacity() == True:
          return "Hangar Capacity Reached!"
        else:
          self.hangar.append(plane)

    def take_off(self, plane):
        if self.weather() != "stormy":
          self.hangar.remove(plane)
        else:
          return "Weather Troubles! No take offs permitted!"

    def weather(self):
        conditions = ["sunny", "overcast", "stormy"]
        return random.choice(conditions)
        
    def full_capacity(self):
        if len(self.hangar) == self.capacity:
            return True
        else:
            return False