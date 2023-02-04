class Shape:

    def __init__(self):
        pass

    def area(self):
        return 0;

    class Square:

        def __init__(self, length):
            self.length = length

        def area(self):
            return self.length**2


a = Shape.Square(8)
print(a.area())
