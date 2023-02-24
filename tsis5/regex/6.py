import re

with open('raw.txt', 'r', encoding='utf8') as file:
    data = file.read()

pattern = '[ ,.]'
print(re.sub(pattern, ":", data))
