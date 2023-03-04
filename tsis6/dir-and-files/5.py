import os

path = input("Enter path: ")
list = list(map(int, input("Enter list: ").split()))

writtenFile = open(path, "a")
writtenFile.write(str(list))
writtenFile.close()
