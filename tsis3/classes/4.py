import math as m


class Point:
    def __init__(self, coord_x, coord_y):
        self.coord_x = coord_x
        self.coord_y = coord_y

    def show(self):
        print(self.coord_x, self.coord_y)

    def move(self, coord_x_new, coord_y_new):
        self.coord_x = coord_x_new
        self.coord_y = coord_y_new

    def distance(self, coord_x_1, coord_y_1, coord_x_2, coord_y_2):
        return m.sqrt((coord_x_2-coord_x_1)**2 + (coord_y_2-coord_y_1)**2)


p = Point(3, 4)
p.show()
p.move(5, 6)
p.show()
print(f"{p.distance(1, 2, 3, 4):.3f}")