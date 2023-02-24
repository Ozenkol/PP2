import re

with open('raw.txt', 'r', encoding='utf8') as file:
    data = file.read()

pattern = '[a-zа-я]+-[a-zа-я]+'
for word in re.finditer(pattern, data):
    print("Word: ", word[0])
