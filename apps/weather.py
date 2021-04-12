import random

class Weather:
    def __init__(self):
        self.conditions = ["sunny", "overcast", "stormy"]
    
    def weather_check(self):
        return random.choice(self.conditions)