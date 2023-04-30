import pygame

pygame.init()
font = pygame.font.SysFont("Comicsans", 20)


class Title_creator():
    def __init__(self, text, x, y, color):
        self.text = text
        self.pos_x = x
        self.pos_y = y
        self.color = color

    def update(self, new_text):
        self.text = new_text

    def draw(self, surface):
        my_text = font.render(self.text, True, self.color)
        surface.blit(my_text, (self.pos_x, self.pos_y))


class your_score():
    def __init__(self, score):
        self.title = Title_creator("Your score "+str(score), 300, 0, (1, 1, 1))

    def update(self, score):
        self.title.text = "Your score "+str(score)

    def draw(self, surface):
        self.title.draw(surface)


class your_level():
    def __init__(self, score):
        self.title = Title_creator("Your level " + str(score), 300, 25, (1, 1, 1))

    def update(self, level):
        self.title.text = "Your level " + str(level)

    def draw(self, surface):
        self.title.draw(surface)


class save_title():
    def __init__(self):
        self.title = Title_creator("Save", 0, 0, (1, 1, 1))

    def draw(self, surface):
        self.title.draw(surface)


class enter_username():
    def __init__(self):
        self.title = Title_creator("Enter username: ", 150, 125, (220, 50, 20))

    def draw(self, surface):
        self.title.draw(surface)