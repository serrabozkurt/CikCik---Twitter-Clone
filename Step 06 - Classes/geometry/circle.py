import math

class Circle:
    def __init__(self, r):
        self.radius = r

    def circumference(self):
        return 2 * math.pi * self.radius

    def area(self):
        return math.pi * (self.radius ** 2)