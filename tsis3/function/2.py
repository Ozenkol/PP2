def from_fahrenheit_to_c(f):
    c = (5 / 9)*(f-32)
    return c


F = int(input())

print(from_fahrenheit_to_c(F))
