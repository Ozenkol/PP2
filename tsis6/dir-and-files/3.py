import os


def existence(path):
    if os.path.exists(path) is True:
        print("Your path exist!")
        print("Your filename of the path:")
        print(os.path.basename(path))
        print("Your directory name of the path:")
        print(os.path.dirname(path))
    else:
        print("Your path doesn't exist!")
