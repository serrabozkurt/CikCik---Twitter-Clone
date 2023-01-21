class Rectangle:
    def __init__(self, a, b):
        self.short = a
        self.long = b

    def area(self):
        return self.short * self.long

    def circumference(self):
        return 2 * (self.short + self.long)


d1 = Rectangle(3, 5)

print(d1.area())
print()

class Square(Rectangle):
    def __init__(self, a):
        self.short = a
        self.long = a


k1 = Square(5)
print(k1.circumference())
print(k1.area())
