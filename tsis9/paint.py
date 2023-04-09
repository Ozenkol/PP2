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


toolchain = pygame.sprite.Group()
colors = pygame.sprite.Group()
color_button_red = Sprite_creator(0, 0, 50, 25, (255, 0, 0))
color_button_blue = Sprite_creator(50, 0, 50, 25, (0, 255, 0))
color_button_green = Sprite_creator(100, 0, 50, 25, (0, 0, 255))
ellipse_button = Sprite_creator(150, 0, 50, 25, (125, 125, 125))
eraser_button = Sprite_creator(200, 0, 50, 25, (125, 125, 35))
rectangle_button = Sprite_creator(250, 0, 50, 25, (125, 35, 35))
toolchain.add(color_button_red)
toolchain.add(color_button_blue)
toolchain.add(color_button_green)
toolchain.add(ellipse_button)
toolchain.add(rectangle_button)
toolchain.add(eraser_button)
colors.add(color_button_red)
colors.add(color_button_blue)
colors.add(color_button_green)

surface = pygame.display.set_mode((500, 500))
color = (255, 255, 255)
done = False
line_drawer = Line_drawer(color)
ellipse_drawer = Ellipse_drawer(color)
rect_drawer = Rectangle_drawer(color)
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
    eraser_text()
    ellipse_text()
    rectangle_text()
    pygame.display.update()
    clock.tick(60)
