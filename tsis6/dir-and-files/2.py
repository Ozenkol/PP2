import os

def existence(path):
    try:
        os.path.exists(path)
        print("Your file exist!\n")
    except:
        print("Your file doesn't exist!\n")


def readability(path):
    try:
        open(path, "r")
        print("Your file readable!\n")
    except:
        print("You don't have ability to read file!\n")



def writability(path):
    try:
        open(path, "w").close()
        print("Your file writable!\n")
    except:
        print("You don't have ability to write file!\n")


def executability(path):
    try:
        os.startfile(path)
        print("Your file executable!\n")
    except:
        print("Your file doesn't executable!\n")


path = input("Enter path of file/directory: ")


existence(path)
readability(path)
writability(path)
executability(path)


