import os

first_file = open("first.txt", "r")
second_file = open("second.txt", "a")

for line in first_file.readlines():
    second_file.write(line)

