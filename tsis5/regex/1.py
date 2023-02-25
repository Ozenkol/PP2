import re

with open("raw.txt", "r", encoding="utf8") as file:
    data = file.read()

pattern = '\w+а{1}б*\w+'

print(re.findall(pattern, data))

#Для проверки
#for word in re.finditer(pattern, data):
#    print("Word: ", word[0])

