txt = "hello, and welcome to my world."
x = txt.capitalize()
print (x)

print()

txt = "python is FUN!"
x = txt.capitalize()
print (x)

print()

txt = "36 is my age."
x = txt.capitalize()
print (x)

print()

txt = "Hello, And Welcome To My World!"
x = txt.casefold()
print(x)

print()

txt = "banana"
x = txt.center(20)
print(x)

print()

txt = "banana"
x = txt.center(20, "O")
print(x)

print()

txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple")
print(x)

print()

txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple", 10, 24)
print(x)

print()

txt = "My name is Ståle"
x = txt.encode()
print(x)

print()

txt = "My name is Ståle"

print(txt.encode(encoding="ascii",errors="backslashreplace"))
print(txt.encode(encoding="ascii",errors="ignore"))
print(txt.encode(encoding="ascii",errors="namereplace"))
print(txt.encode(encoding="ascii",errors="replace"))
print(txt.encode(encoding="ascii",errors="xmlcharrefreplace"))

print()

txt = "Hello, welcome to my world."
x = txt.endswith(".")
print(x)

print()

txt = "Hello, welcome to my world."
x = txt.endswith("my world.")
print(x)

print()

txt = "Hello, welcome to my world."
x = txt.endswith("my world.", 5, 11)
print(x)

print()

txt = "H\te\tl\tl\to"
x =  txt.expandtabs(2)
print(x)

print()

txt = "H\te\tl\tl\to"
print(txt)
print(txt.expandtabs())
print(txt.expandtabs(2))
print(txt.expandtabs(4))
print(txt.expandtabs(10))

print()

txt = "Hello, welcome to my world."
x = txt.find("welcome")
print(x)

print()

txt = "Hello, welcome to my world."
x = txt.find("e")
print(x)

print()

txt = "Hello, welcome to my world."
x = txt.find("e", 5, 10)
print(x)

print()

txt = "Hello, welcome to my world."
print(txt.find("q"))
print(txt.index("q"))

print()


