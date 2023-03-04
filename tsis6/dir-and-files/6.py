import string


def generateABCFiles():
    for letter in string.ascii_uppercase:
        open(letter+".txt", "w")


generateABCFiles()