import pygame


class Level_creator(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.rect_list = []

    def rectangles_adder(self, x, y, width, height):
        self.rect_list.append(pygame.rect.Rect((x, y, width, height)))

    def rectangle_clear(self):
        self.rect_list = []

    def draw(self, surface):
        for rectangle in self.rect_list:
            pygame.draw.rect(surface, (0, 255, 0), rectangle)


