import re

with open('raw.txt', 'r', encoding='utf8') as file:
    data = file.read()

pattern = '[A-ZА-Я][a-zа-я]\w+'

for word in re.finditer(pattern, data):
    print("Word: ", word[0])