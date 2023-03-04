import os


def existence(path):
    try:
        os.path.exists(path)
        return True
    except:
        return False


def readability(path):
    try:
        open(path, "r")
        return True
    except:
        return False


def writability(path):
    try:
        open(path, "w").close()
        return True
    except:
        return False


current_path = os.getcwd()
file_name = input("Enter filename: ")
path = os.path.join(current_path, file_name)

if existence(path)==True:
    os.remove(path)
    print(f"Your file {file_name} was deleted\n")

else:
    print("Your file doesn't exist or you don't have access\n")


