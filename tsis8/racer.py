import pygame
import random
import time
import sys


pygame.init()

score = 0
surface = pygame.display.set_mode((500, 500))
my_font = pygame.font.SysFont("Verdana", 25)
background = pygame.image.load("src/bg.jpg")
background = pygame.transform.scale(background, (500, 500))
game_over = my_font.render("GAME OVER", True, (1, 1, 1))


def Score(score, surface):
    your_score = my_font.render("YOUR SCORE " + str(score), True, (1, 1, 1))
    surface.blit(your_score, (500 - your_score.get_rect().topright[0], 0))


class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.rect = pygame.rect.Rect((0, 0, 20, 20))
        self.rect.center = (random.randint(40, 460), 0)

    def update(self):
        self.rect.move_ip(0, 5)
        if self.rect.bottom > 500:
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)

    def draw(self, surface):
        pygame.draw.circle(surface, (255, 255, 0), self.rect.center, 10)


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("src/enemy_car.png")
        self.image = pygame.transform.scale(self.image, (50, 100))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(50, 450), 0)

    def update(self):
        self.rect.move_ip(0, 2)
        global score
        if self.rect.bottom > 500:
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("src/my_car.png")
        self.image = pygame.transform.scale(self.image, (50, 100))
        self.rect = self.image.get_rect()
        self.rect.center = (250, 450)

    def update(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[pygame.K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < 500:
            if pressed_keys[pygame.K_RIGHT]:
                self.rect.move_ip(5, 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)


my_car = Player()
enemy_car = Enemy()
my_coin = Coin()

enemies = pygame.sprite.Group()
enemies.add(enemy_car)
all_sprites = pygame.sprite.Group()
all_sprites.add(my_car)
all_sprites.add(enemy_car)
all_sprites.add(my_coin)
points = pygame.sprite.Group()
points.add(my_coin)

done = False
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        print(game_over.get_rect().center)
        if event.type == pygame.QUIT:
            done = True
    surface.blit(background, (0, 0))

    Score(score, surface)

    for entity in all_sprites:
        if entity != my_coin:
            surface.blit(entity.image, entity.rect)
        else:
            entity.draw(surface)
        entity.update()

    if pygame.sprite.spritecollideany(my_car, enemies):
        pygame.mixer.Sound("src/crash.mp3").play()
        time.sleep(5)
        surface.fill((255, 0, 0))
        surface.blit(game_over, (250 - game_over.get_rect().center[0], 250 - game_over.get_rect().center[1]))
        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    if pygame.sprite.spritecollideany(my_car, points):
        for entity in all_sprites:
            if entity == my_coin:
                entity.kill()
                score = score + 1
        my_coin = Coin()
        all_sprites.add(my_coin)
        points.add(my_coin)

    pygame.display.update()
    clock.tick(60)
