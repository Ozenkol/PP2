import re

# with open('raw.txt', 'r', encoding='utf8') as file:
#     data = file.read()
text = input()
pattern = '[_][a-z]'
print(re.sub(pattern, ' ', text))
