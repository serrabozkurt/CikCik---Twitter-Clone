from example1 import Square, d1

kare = Square(3)
print(kare.area())

print(d1.circumference())


import math

print(math.pi)

import random
from random import shuffle

print(random.randint(0, 10))

renkler = ["turuncu", "beyaz", "yeşil", "siyah", "sarı", "mavi"]
print(random.choice(renkler))

print(renkler)
orijinal = renkler.copy()
shuffle(renkler)
print(renkler)
print(renkler[:3])

class Circle:
    r = 0

from geometry.circle import Circle as C2

d = Circle()
d2 = C2(5)
