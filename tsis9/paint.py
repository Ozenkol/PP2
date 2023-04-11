import math

import pygame

pygame.init()

font = pygame.font.SysFont("Comicsans", 15)


def eraser_text():
    eraser_text = font.render("Eraser ", True, (1, 1, 1))
    surface.blit(eraser_text, (200, 0))


def ellipse_text():
    ellipse_text = font.render("Ellipse ", True, (1, 1, 1))
    surface.blit(ellipse_text, (150, 0))


def rectangle_text():
    rectangle_text = font.render("Rect ", True, (1, 1, 1))
    surface.blit(rectangle_text, (250, 0))


def r_tr_text():
    rectangle_text = font.render("R.tri ", True, (1, 1, 1))
    surface.blit(rectangle_text, (300, 0))


def eq_tr_text():
    rectangle_text = font.render("Eq.tri ", True, (1, 1, 1))
    surface.blit(rectangle_text, (350, 0))


def rhombus_text():
    rectangle_text = font.render("Rhomb ", True, (1, 1, 1))
    surface.blit(rectangle_text, (400, 0))


def square_text():
    square_text = font.render("Square", True, (1, 1, 1))
    surface.blit(square_text, (450, 0))


class Square(pygame.sprite.Sprite):
    def __init__(self, color):
        super().__init__()
        self.color = color
        self.pressed = False
        self.mouse_pos_1 = None
        self.mouse_pos_2 = None
        self.start_x = None
        self.start_y = None
        self.end_x = None
        self.end_y = None
        self.start_x_cat_1 = None
        self.start_y_cat_1 = None
        self.end_x_cat_1 = None
        self.end_y_cat_1 = None
        self.start_x_cat_2 = None
        self.start_y_cat_2 = None
        self.end_x_cat_2 = None
        self.end_y_cat_2 = None

    def draw(self, surface):
        mouse_pressed = pygame.mouse.get_pressed()
        if mouse_pressed[0] and not self.pressed:
            self.pressed = True
            self.mouse_pos_1 = pygame.mouse.get_pos()

        if self.pressed and not mouse_pressed[0]:
            self.mouse_pos_2 = pygame.mouse.get_pos()
            self.pressed = not self.pressed
        if self.mouse_pos_2 is not None and self.mouse_pos_1 is not None:
            width = (self.mouse_pos_2[0] - self.mouse_pos_1[0])
            height = (self.mouse_pos_2[1] - self.mouse_pos_1[1])
            self.start_x = self.mouse_pos_1[0]
            self.start_y = self.mouse_pos_1[1]
            self.end_x = self.mouse_pos_2[0]
            self.end_y = self.mouse_pos_2[1]

            if self.mouse_pos_1 is not None and self.mouse_pos_2 is not None:
                pygame.draw.line(surface, self.color, (self.start_x, self.start_y), (self.end_x, self.end_y), 5)
                pygame.draw.line(surface, self.color, (self.end_x, self.end_y),
                                 (self.end_x + height, self.end_y - width), 5)
                pygame.draw.line(surface, self.color, (self.start_x, self.start_y),
                                 (self.start_x + height, self.start_y - width), 5)
                pygame.draw.line(surface, self.color, (self.end_x + height, self.end_y - width),
                                 (self.start_x + height, self.start_y - width), 5)

                self.mouse_pos_1 = None
                self.mouse_pos_2 = None


class Rhombus(pygame.sprite.Sprite):
    def __init__(self, color):
        super().__init__()
        self.color = color
        self.pressed = False
        self.mouse_pos_1 = None
        self.mouse_pos_2 = None
        self.start_x = None
        self.start_y = None
        self.end_x = None
        self.end_y = None
        self.start_x_cat_1 = None
        self.start_y_cat_1 = None
        self.end_x_cat_1 = None
        self.end_y_cat_1 = None
        self.start_x_cat_2 = None
        self.start_y_cat_2 = None
        self.end_x_cat_2 = None
        self.end_y_cat_2 = None

    def draw(self, surface):
        mouse_pressed = pygame.mouse.get_pressed()
        if mouse_pressed[0] and not self.pressed:
            self.pressed = True
            self.mouse_pos_1 = pygame.mouse.get_pos()

        if self.pressed and not mouse_pressed[0]:
            self.mouse_pos_2 = pygame.mouse.get_pos()
            self.pressed = not self.pressed
        if self.mouse_pos_2 is not None and self.mouse_pos_1 is not None:
            self.start_x = self.mouse_pos_1[0]
            self.start_y = self.mouse_pos_1[1]
            self.end_x = self.mouse_pos_2[0]
            self.end_y = self.mouse_pos_2[1]

            if self.mouse_pos_1 is not None and self.mouse_pos_2 is not None:
                width = (self.mouse_pos_2[0] - self.mouse_pos_1[0])
                height = (self.mouse_pos_2[1] - self.mouse_pos_1[1])
                pygame.draw.line(surface, self.color, (self.start_x, self.start_y), (self.end_x, self.end_y), 5)
                pygame.draw.line(surface, self.color, (self.end_x, self.end_y), (self.end_x + width, self.end_y - height), 5)
                pygame.draw.line(surface, self.color, (self.start_x, self.start_y), (self.start_x + width, self.start_y - height), 5)
                pygame.draw.line(surface, self.color, (self.end_x + width, self.end_y - height), (self.start_x + width, self.start_y - height), 5)

                self.mouse_pos_1 = None
                self.mouse_pos_2 = None



class Sprite_creator(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color):
        super().__init__()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.clicked = False
        self.rect = pygame.rect.Rect((x, y, width, height))
        self.clicked_rect = pygame.rect.Rect((x, y, width, height))

    def update(self, event_list):
        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.rect.collidepoint(event.pos):
                    self.clicked = not self.clicked

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height))
        if self.clicked:
            pygame.draw.rect(surface, (0, 0, 0), self.clicked_rect, 2)


class Rectangle_drawer(pygame.sprite.Sprite):
    def __init__(self, color):
        super().__init__()
        self.color = color
        self.pressed = False
        self.mouse_pos_1 = None
        self.mouse_pos_2 = None

    def draw(self, surface):
        mouse_pressed = pygame.mouse.get_pressed()
        if mouse_pressed[0] and not self.pressed:
            self.pressed = True
            self.mouse_pos_1 = pygame.mouse.get_pos()
        if self.pressed and not mouse_pressed[0]:
            self.mouse_pos_2 = pygame.mouse.get_pos()
            self.pressed = not self.pressed
        if self.mouse_pos_2 is not None and self.mouse_pos_1 is not None:
            width = abs(self.mouse_pos_2[0] - self.mouse_pos_1[0])
            height = abs(self.mouse_pos_2[1] - self.mouse_pos_1[1])
            if self.mouse_pos_2 < self.mouse_pos_1:
                if self.mouse_pos_1[1] < self.mouse_pos_2[1]:
                    self.top_left = (self.mouse_pos_1[0] - width, self.mouse_pos_1[1])
                if self.mouse_pos_2[1] < self.mouse_pos_1[1]:
                    self.top_left = self.mouse_pos_2
            if self.mouse_pos_1 < self.mouse_pos_2:
                if self.mouse_pos_1[1] < self.mouse_pos_2[1]:
                    self.top_left = self.mouse_pos_1
                if self.mouse_pos_2[1] < self.mouse_pos_1[1]:
                    self.top_left = (self.mouse_pos_2[0] - width, self.mouse_pos_2[1])
            if self.mouse_pos_1 == self.mouse_pos_2:
                self.top_left = (0, 0)

            if self.top_left is not None: pygame.draw.rect(surface, self.color, self.top_left+(width, height), 5)
            self.mouse_pos_1 = None
            self.mouse_pos_2 = None


class Ellipse_drawer(pygame.sprite.Sprite):
    def __init__(self, color):
        super().__init__()
        self.color = color
        self.pressed = False
        self.mouse_pos_1 = None
        self.mouse_pos_2 = None
        self.top_left = None

    def draw(self, surface):
        mouse_pressed = pygame.mouse.get_pressed()
        if mouse_pressed[0] and not self.pressed:
            self.pressed = True
            self.mouse_pos_1 = pygame.mouse.get_pos()

        if self.pressed and not mouse_pressed[0]:
            self.mouse_pos_2 = pygame.mouse.get_pos()
            self.pressed = not self.pressed
        if self.mouse_pos_2 is not None and self.mouse_pos_1 is not None:
            width = abs(self.mouse_pos_2[0] - self.mouse_pos_1[0])
            height = abs(self.mouse_pos_2[1] - self.mouse_pos_1[1])
            if self.mouse_pos_2 < self.mouse_pos_1:
                if self.mouse_pos_1[1] < self.mouse_pos_2[1]:
                    self.top_left = (self.mouse_pos_1[0] - width, self.mouse_pos_1[1])
                if self.mouse_pos_2[1] < self.mouse_pos_1[1]:
                    self.top_left = self.mouse_pos_2
            if self.mouse_pos_1 < self.mouse_pos_2:
                if self.mouse_pos_1[1] < self.mouse_pos_2[1]:
                    self.top_left = self.mouse_pos_1
                if self.mouse_pos_2[1] < self.mouse_pos_1[1]:
                    self.top_left = (self.mouse_pos_2[0] - width, self.mouse_pos_2[1])
            if self.mouse_pos_1 == self.mouse_pos_2:
                self.top_left = (0, 0)

            if self.top_left is not None:
                pygame.draw.ellipse(surface, self.color, self.top_left + (width, height), 5)
            self.mouse_pos_1 = None
            self.mouse_pos_2 = None


class Line_drawer(pygame.sprite.Sprite):
    def __init__(self, color):
        super().__init__()
        self.color = color

    def draw(self, surface):
        mouse_pressed = pygame.mouse.get_pressed()
        mouse_pos = pygame.mouse.get_pos()
        if mouse_pressed[0]:
            pygame.draw.rect(surface, self.color, mouse_pos + (10, 10))


class Right_triangle(pygame.sprite.Sprite):
    def __init__(self, color):
        super().__init__()
        self.color = color
        self.pressed = False
        self.mouse_pos_1 = None
        self.mouse_pos_2 = None
        self.start_x = None
        self.start_y = None
        self.end_x = None
        self.end_y = None
        self.start_x_cat_1 = None
        self.start_y_cat_1 = None
        self.end_x_cat_1 = None
        self.end_y_cat_1 = None
        self.start_x_cat_2 = None
        self.start_y_cat_2 = None
        self.end_x_cat_2 = None
        self.end_y_cat_2 = None

    def draw(self, surface):
        mouse_pressed = pygame.mouse.get_pressed()
        if mouse_pressed[0] and not self.pressed:
            self.pressed = True
            self.mouse_pos_1 = pygame.mouse.get_pos()

        if self.pressed and not mouse_pressed[0]:
            self.mouse_pos_2 = pygame.mouse.get_pos()
            self.pressed = not self.pressed
        if self.mouse_pos_2 is not None and self.mouse_pos_1 is not None:
            width = abs(self.mouse_pos_2[0] - self.mouse_pos_1[0])
            height = abs(self.mouse_pos_2[1] - self.mouse_pos_1[1])
            self.start_x = self.mouse_pos_1[0]
            self.start_y = self.mouse_pos_1[1]
            self.end_x = self.mouse_pos_2[0]
            self.end_y = self.mouse_pos_2[1]
            if self.mouse_pos_2 < self.mouse_pos_1:
                if self.mouse_pos_1[1] < self.mouse_pos_2[1]:
                    self.start_x_cat_1 = self.mouse_pos_1[0]
                    self.start_y_cat_1 = self.mouse_pos_1[1]
                    self.end_x_cat_1 = self.mouse_pos_1[0] - width
                    self.end_y_cat_1 = self.mouse_pos_1[1]
                    self.start_x_cat_2 = self.mouse_pos_2[0]
                    self.start_y_cat_2 = self.mouse_pos_2[1]
                    self.end_x_cat_2 = self.mouse_pos_2[0]
                    self.end_y_cat_2 = self.mouse_pos_2[1] - height
                if self.mouse_pos_2[1] < self.mouse_pos_1[1]:
                    self.start_x_cat_1 = self.mouse_pos_1[0]
                    self.start_y_cat_1 = self.mouse_pos_1[1]
                    self.end_x_cat_1 = self.mouse_pos_1[0]
                    self.end_y_cat_1 = self.mouse_pos_1[1] - height
                    self.start_x_cat_2 = self.mouse_pos_2[0]
                    self.start_y_cat_2 = self.mouse_pos_2[1]
                    self.end_x_cat_2 = self.mouse_pos_1[0]
                    self.end_y_cat_2 = self.mouse_pos_1[1] - height
            if self.mouse_pos_1 < self.mouse_pos_2:
                if self.mouse_pos_1[1] < self.mouse_pos_2[1]:
                    self.start_x_cat_1 = self.mouse_pos_1[0]
                    self.start_y_cat_1 = self.mouse_pos_1[1]
                    self.end_x_cat_1 = self.mouse_pos_1[0]
                    self.end_y_cat_1 = self.mouse_pos_1[1] + height
                    self.start_x_cat_2 = self.mouse_pos_2[0]
                    self.start_y_cat_2 = self.mouse_pos_2[1]
                    self.end_x_cat_2 = self.mouse_pos_2[0] - width
                    self.end_y_cat_2 = self.mouse_pos_2[1]
                if self.mouse_pos_2[1] < self.mouse_pos_1[1]:
                    self.start_x_cat_1 = self.mouse_pos_1[0]
                    self.start_y_cat_1 = self.mouse_pos_1[1]
                    self.end_x_cat_1 = self.mouse_pos_1[0] + width
                    self.end_y_cat_1 = self.mouse_pos_1[1]
                    self.start_x_cat_2 = self.mouse_pos_2[0]
                    self.start_y_cat_2 = self.mouse_pos_2[1]
                    self.end_x_cat_2 = self.mouse_pos_2[0]
                    self.end_y_cat_2 = self.mouse_pos_2[1] + height
            if self.mouse_pos_1 == self.mouse_pos_2:
                self.start_x_cat_1 = 0
                self.start_y_cat_1 = 0
                self.end_x_cat_1 = 0
                self.end_y_cat_1 = 0
                self.start_x_cat_2 = 0
                self.start_y_cat_2 = 0
                self.end_x_cat_2 = 0
                self.end_y_cat_2 = 0

            if self.mouse_pos_1 is not None and self.mouse_pos_2 is not None:
                pygame.draw.line(surface, self.color, (self.start_x, self.start_y), (self.end_x, self.end_y), 5)
                pygame.draw.line(surface, self.color, (self.start_x_cat_1, self.start_y_cat_1), (self.end_x_cat_1, self.end_y_cat_1), 5)
                pygame.draw.line(surface, self.color, (self.start_x_cat_2, self.start_y_cat_2), (self.end_x_cat_2, self.end_y_cat_2), 5)
                self.mouse_pos_1 = None
                self.mouse_pos_2 = None


class Equilateral_triangle(pygame.sprite.Sprite):
    def __init__(self, color):
        super().__init__()
        self.color = color
        self.pressed = False
        self.mouse_pos_1 = None
        self.mouse_pos_2 = None
        self.start_x = None
        self.start_y = None
        self.end_x = None
        self.end_y = None
        self.start_x_cat_1 = None
        self.start_y_cat_1 = None
        self.end_x_cat_1 = None
        self.end_y_cat_1 = None
        self.start_x_cat_2 = None
        self.start_y_cat_2 = None
        self.end_x_cat_2 = None
        self.end_y_cat_2 = None

    def draw(self, surface):
        mouse_pressed = pygame.mouse.get_pressed()
        if mouse_pressed[0] and not self.pressed:
            self.pressed = True
            self.mouse_pos_1 = pygame.mouse.get_pos()

        if self.pressed and not mouse_pressed[0]:
            self.mouse_pos_2 = pygame.mouse.get_pos()
            self.pressed = not self.pressed
        if self.mouse_pos_2 is not None and self.mouse_pos_1 is not None:
            width = (self.mouse_pos_2[0] - self.mouse_pos_1[0])
            height = (self.mouse_pos_2[1] - self.mouse_pos_1[1])
            self.start_x = self.mouse_pos_1[0]
            self.start_y = self.mouse_pos_1[1]
            self.end_x = self.mouse_pos_2[0]
            self.end_y = self.mouse_pos_2[1]
            center_x = (self.start_x + self.end_x) / 2
            center_y = (self.start_y + self.end_y) / 2
            side = math.sqrt(width**2 + height**2)
            if self.mouse_pos_2 < self.mouse_pos_1:
                if self.mouse_pos_1[1] < self.mouse_pos_2[1]:
                    self.start_x_cat_1 = self.mouse_pos_1[0]
                    self.start_y_cat_1 = self.mouse_pos_1[1]
                    self.end_x_cat_1 = center_x - int((math.sqrt(3) / 2) * height )
                    self.end_y_cat_1 = center_y + int((math.sqrt(3) / 2) * width )
                    self.start_x_cat_2 = self.mouse_pos_2[0]
                    self.start_y_cat_2 = self.mouse_pos_2[1]
                    self.end_x_cat_2 = center_x - int((math.sqrt(3) / 2) * height)
                    self.end_y_cat_2 = center_y + int((math.sqrt(3) / 2) * width)
                if self.mouse_pos_2[1] < self.mouse_pos_1[1]:
                    self.start_x_cat_1 = self.mouse_pos_1[0]
                    self.start_y_cat_1 = self.mouse_pos_1[1]
                    self.end_x_cat_1 = center_x - int((math.sqrt(3) / 2) * height)
                    self.end_y_cat_1 = center_y + int((math.sqrt(3) / 2) * width)
                    self.start_x_cat_2 = self.mouse_pos_2[0]
                    self.start_y_cat_2 = self.mouse_pos_2[1]
                    self.end_x_cat_2 = center_x - int((math.sqrt(3) / 2) * height)
                    self.end_y_cat_2 = center_y + int((math.sqrt(3) / 2) * width)
            if self.mouse_pos_1 < self.mouse_pos_2:
                if self.mouse_pos_1[1] < self.mouse_pos_2[1]:
                    self.start_x_cat_1 = self.mouse_pos_1[0]
                    self.start_y_cat_1 = self.mouse_pos_1[1]
                    self.end_x_cat_1 = center_x - int((math.sqrt(3) / 2) * height)
                    self.end_y_cat_1 = center_y + int((math.sqrt(3) / 2) * width)
                    self.start_x_cat_2 = self.mouse_pos_2[0]
                    self.start_y_cat_2 = self.mouse_pos_2[1]
                    self.end_x_cat_2 = center_x - int((math.sqrt(3) / 2) * height)
                    self.end_y_cat_2 = center_y + int((math.sqrt(3) / 2) * width)
                if self.mouse_pos_2[1] < self.mouse_pos_1[1]:
                    self.start_x_cat_1 = self.mouse_pos_1[0]
                    self.start_y_cat_1 = self.mouse_pos_1[1]
                    self.end_x_cat_1 = center_x - int((math.sqrt(3) / 2) * height)
                    self.end_y_cat_1 = center_y + int((math.sqrt(3) / 2) * width)
                    self.start_x_cat_2 = self.mouse_pos_2[0]
                    self.start_y_cat_2 = self.mouse_pos_2[1]
                    self.end_x_cat_2 = center_x - int((math.sqrt(3) / 2) * height)
                    self.end_y_cat_2 = center_y + int((math.sqrt(3) / 2) * width)
            if self.mouse_pos_1 == self.mouse_pos_2:
                self.start_x = 0
                self.start_y = 0
                self.end_x = 0
                self.end_y = 0
                self.start_x_cat_2 = 0
                self.start_y_cat_2 = 0
                self.end_x_cat_2 = 0
                self.end_y_cat_2 = 0
                self.start_x_cat_1 = 0
                self.start_y_cat_1 = 0
                self.end_x_cat_1 = 0
                self.end_y_cat_1 = 0

            if self.mouse_pos_1 is not None and self.mouse_pos_2 is not None:
                pygame.draw.line(surface, self.color, (self.start_x, self.start_y), (self.end_x, self.end_y), 5)
                pygame.draw.line(surface, self.color, (self.start_x_cat_1, self.start_y_cat_1),
                                 (self.end_x_cat_1, self.end_y_cat_1), 5)
                pygame.draw.line(surface, self.color, (self.start_x_cat_2, self.start_y_cat_2),
                                 (self.end_x_cat_2, self.end_y_cat_2), 5)
                self.mouse_pos_1 = None
                self.mouse_pos_2 = None


toolchain = pygame.sprite.Group()
colors = pygame.sprite.Group()
color_button_red = Sprite_creator(0, 0, 50, 25, (255, 0, 0))
color_button_blue = Sprite_creator(50, 0, 50, 25, (0, 255, 0))
color_button_green = Sprite_creator(100, 0, 50, 25, (0, 0, 255))
ellipse_button = Sprite_creator(150, 0, 50, 25, (125, 125, 125))
eraser_button = Sprite_creator(200, 0, 50, 25, (125, 125, 35))
rectangle_button = Sprite_creator(250, 0, 50, 25, (125, 35, 35))
right_triangle_button = Sprite_creator(300, 0, 50, 25, (111, 111, 111))
eq_triangle_button = Sprite_creator(350, 0, 50, 25, (122, 122, 45))
rhombus_button = Sprite_creator(400, 0, 50, 25, (144, 63, 12))
square_button = Sprite_creator(450, 0, 50, 25, (123, 122, 98))
toolchain.add(rhombus_button)
toolchain.add(square_button)
toolchain.add(right_triangle_button)
toolchain.add(color_button_red)
toolchain.add(color_button_blue)
toolchain.add(color_button_green)
toolchain.add(ellipse_button)
toolchain.add(rectangle_button)
toolchain.add(eraser_button)
toolchain.add(eq_triangle_button)
colors.add(color_button_red)
colors.add(color_button_blue)
colors.add(color_button_green)

surface = pygame.display.set_mode((500, 500))
color = (255, 255, 255)
done = False
line_drawer = Line_drawer(color)
ellipse_drawer = Ellipse_drawer(color)
rect_drawer = Rectangle_drawer(color)
right_triangle_drawer = Right_triangle(color)
eq_triangle_drawer = Equilateral_triangle(color)
rhombus_drawer = Rhombus(color)
square_drawer = Square(color)
drawers = pygame.sprite.Group()
drawers.add(line_drawer)
drawers.add(square_drawer)
drawers.add(rhombus_drawer)
drawers.add(ellipse_drawer)
drawers.add(rect_drawer)
drawers.add(right_triangle_drawer)
drawers.add(eq_triangle_drawer)
clock = pygame.time.Clock()
color_button_red.clicked = True

surface.fill((255, 255, 255))

while not done:
    event_list = pygame.event.get()

    for event in event_list:
        if event.type == pygame.QUIT:
            done = True

    for entity in toolchain:
        entity.update(event_list)
        entity.draw(surface)

    if color_button_red.clicked:
        color = (255, 0, 0)
    if color_button_blue.clicked:
        color = (0, 255, 0)
    if color_button_green.clicked:
        color = (0, 0, 255)
    if ellipse_button.clicked:
        ellipse_drawer.color = color
        ellipse_drawer.draw(surface)
    if eraser_button.clicked:
        line_drawer.color = (255, 255, 255)
        line_drawer.draw(surface)
    if rectangle_button.clicked:
        rect_drawer.color = color
        rect_drawer.draw(surface)
    if right_triangle_button.clicked:
        right_triangle_drawer.color = color
        right_triangle_drawer.draw(surface)
    if eq_triangle_button.clicked:
        eq_triangle_drawer.color = color
        eq_triangle_drawer.draw(surface)
    if rhombus_button.clicked:
        rhombus_drawer.color = color
        rhombus_drawer.draw(surface)
    if square_button.clicked:
        square_drawer.color = color
        square_drawer.draw(surface)
    eraser_text()
    ellipse_text()
    rectangle_text()
    r_tr_text()
    eq_tr_text()
    rhombus_text()
    square_text()
    pygame.display.update()
    clock.tick(60)
