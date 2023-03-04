import os
import re

path = input()
print("All files of directory:", end=" ")
print(*os.listdir(path=path), sep=", ")

print("All directories: ", re.findall(r'\w+[^.]\w', str(os.listdir(path=path))))
print("All files: ", re.findall(r"\w+[.]\w+", str(os.listdir(path=path))))
