class some_class:
    def __init__(self):
        self.string = ""

    def getString(self):
        self.string = input()

    def printString(self):
        print(self.string.upper())


a = some_class()

a.getString()
a.printString()
