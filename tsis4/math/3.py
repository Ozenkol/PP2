import math as m

n = int(input("Input number of sides: "))
s = int(input("Input the length of a side: "))

print(f"The area of the polygon is: {((s**2 * n) / (4 * m.tan(m.pi/n))):.3f}")
