#radian
import math

a = int(input())
print(math.radians(a))

#area of a trapezoid.
import math

h = int(input("Height: "))
a = int(input("1st base: "))
b = int(input("2nd base: "))

print(((a + b) / 2) * h)

#area of regular polygon.
import math

n = int(input("Number of sides: "))
s = float(input("Length of a side: "))

area = (n * s**2) / (4 * math.tan(math.pi / n))

print(round(area, 3))

# area of a parallelogram.
b = int(input("base: "))
h = int(input("height: "))

print(h * b)

