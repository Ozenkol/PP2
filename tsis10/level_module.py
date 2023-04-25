import pygame
import random
import snakedatabase

pygame.init()
clock = pygame.time.Clock()
FONT = pygame.font.Font(None, 32)


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
            pygame.draw.rect(surface, (255, 0, 0), rectangle)


class Levels():
    def __init__(self, Level, width, height):
        self.Level = Level
        self.Level_1 = Level_creator()
        self.Level_1.rectangles_adder(0, 0, random.randint(0, width), 5)
        self.Level_1.rectangles_adder(0, 0, random.randint(0, height), 5)
        self.Level_2 = Level_creator()
        self.Level_1.rectangles_adder(50, 0, random.randint(0, width), 5)
        self.Level_1.rectangles_adder(0, 50, random.randint(0, height), 5)
        self.Level_3 = Level_creator()
        self.Level_1.rectangles_adder(100, 0, random.randint(0, width), 5)
        self.Level_1.rectangles_adder(0, 100, random.randint(0, height), 5)
        self.Level_4 = Level_creator()
        self.Level_1.rectangles_adder(20, 0, random.randint(0, width), 5)
        self.Level_1.rectangles_adder(20, 0, random.randint(0, height), 5)
        self.Level_5 = Level_creator()
        self.Level_1.rectangles_adder(10, 0, random.randint(0, width), 5)
        self.Level_1.rectangles_adder(0, 10, random.randint(0, height), 5)

    def return_level(self):
        if self.Level == 1:
            return self.Level_1
        elif self.Level == 2:
            return self.Level_2
        elif self.Level == 3:
            return self.Level_3
        elif self.Level == 4:
            return self.Level_4
        elif self.Level == 5:
            return self.Level_5
        else:
            pass


class InputBox:
    def __init__(self, x, y, w, h, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = (255, 255, 0)
        self.text = text
        self.enter_text = None
        self.id = None
        self.is_username_exist = None
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False
        self.enter = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
            self.color = (122, 222, 2) if self.active else (233, 0, 0)
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    if self.active:
                        if event.key == pygame.K_RETURN:
                            self.enter_text = self.text
                            self.text = ''
                        elif event.key == pygame.K_BACKSPACE:
                            self.text = self.text[:-1]
                        else:
                            self.text += event.unicode
                        self.txt_surface = FONT.render(self.text, True, self.color)
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        pygame.draw.rect(screen, self.color, self.rect, 2)


class Main_menu(pygame.sprite.Sprite):
    def __init__(self, surface):
        self.active = True
        self.id = None
        self.surface = surface
        self.input_box = InputBox(200, 200, 150, 50)

    def update(self, event):
        self.input_box.handle_event(event)
            #print(self.input_box.text, self.input_box.enter_text)
        self.input_box.update()
        if self.input_box.enter_text is not None:
            if snakedatabase.is_username_exist(self.input_box.enter_text):
                id = snakedatabase.get_id(self.input_box.enter_text)
                print(snakedatabase.get_scores_by_id(id))
            else:
                print("Created new user: ")
                snakedatabase.insert_username(self.input_box.enter_text)
                self.id =  snakedatabase.get_id(self.input_box.enter_text)
                self.active = False
            self.input_box.enter_text = None

    def draw(self):
        self.surface.fill((15, 15, 15))
        self.input_box.draw(self.surface)
        pygame.display.flip()




class Button_creator(pygame.sprite.Sprite):
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


class save_button():
    def __init__(self):
        self.button = Button_creator(0, 0, 50, 25, (0, 255, 0))

    def update(self, event_list):
        self.button.update(event_list)

    def draw(self, surface):
        self.button.draw(surface)


