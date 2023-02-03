fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

print()

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)

print()

for x in range(6):
  print(x)

print()

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        break
print(x)