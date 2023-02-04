fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print(fruits)

print()

a = ["apple", "banana", "cherry"]
b = ["Ford", "BMW", "Volvo"]
a.append(b)
print(a)

print()

fruits = ["apple", "banana", "cherry"]
fruits.clear()
print(fruits)

print()

fruits = ["apple", "banana", "cherry"]
x = fruits.copy()
print(x)

print()

fruits = ["apple", "banana", "cherry"]
x = fruits.count("cherry")
print(x)

print()

fruits = [1, 4, 2, 9, 7, 8, 9, 3, 1]
x = fruits.count(9)
print(x)

print()

fruits = ['apple', 'banana', 'cherry']
cars = ['Ford', 'BMW', 'Volvo']
fruits.extend(cars)
print(fruits)

print()

fruits = ['apple', 'banana', 'cherry']
points = (1, 4, 5, 9)
fruits.extend(points)
print(fruits)

print()

fruits = ['apple', 'banana', 'cherry']
x = fruits.index("cherry")
print(x)

print()

fruits = [4, 55, 64, 32, 16, 32]
x = fruits.index(32)
print(x)

print()

fruits = ['apple', 'banana', 'cherry']
fruits.insert(1, "orange")
print(fruits)

print()

fruits = ['apple', 'banana', 'cherry']
fruits.pop(1)
print(fruits)

print()

fruits = ['apple', 'banana', 'cherry']
x = fruits.pop(1)
print(x)

print()

fruits = ['apple', 'banana', 'cherry']
fruits.remove("banana")
print(fruits)

print()

fruits = ['apple', 'banana', 'cherry']
fruits.reverse()
print(fruits)

print()

cars = ['Ford', 'BMW', 'Volvo']
cars.sort()
print(cars)

print()

cars = ['Ford', 'BMW', 'Volvo']
cars.sort(reverse=True)

print()

# A function that returns the length of the value:
def myFunc(e):
  return len(e)
cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']
cars.sort(key=myFunc)
print(cars)

print()

# A function that returns the 'year' value:
def myFunc(e):
  return e['year']
cars = [
  {'car': 'Ford', 'year': 2005},
  {'car': 'Mitsubishi', 'year': 2000},
  {'car': 'BMW', 'year': 2019},
  {'car': 'VW', 'year': 2011}
]
cars.sort(key=myFunc)
print(cars)

print()

# A function that returns the length of the value:
def myFunc(e):
  return len(e)
cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']
cars.sort(reverse=True, key=myFunc)
print(cars)