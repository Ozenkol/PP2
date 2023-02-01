print(10 > 9)
print(10 == 9)
print(10 < 9)

print()

a = 200
b = 33

if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")

print()

print(bool("Hello"))
print(bool(15))

print()

x = "Hello"
y = 15

print(bool(x))
print(bool(y))

print()
####
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])
####
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})
####
class myclass():
    def __len__(self):
        return 0

myobj = myclass()
print(bool(myobj))

print()

def myFunction() :
    return True

print(myFunction())

def myFunction() :
    return True

if myFunction():
    print("YES!")
else:
    print("NO!")

print()

x = 200
print(isinstance(x, int))