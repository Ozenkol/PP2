def is_palyndrome(string):
    return string == string[::-1]


string = input()

print(is_palyndrome(string))
