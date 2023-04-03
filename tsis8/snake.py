import pygame
import random
import level_module

pygame.init()

# system_variables
font = pygame.font.SysFont("Comicsans", 20)
marker = True
width = 500
height = 500
score = 0
level = 1
clock = pygame.time.Clock()


def your_score(score):
    your_score = font.render("Your score "+str(score), True, (1, 1, 1))
    surface.blit(your_score, (width - your_score.get_rect().right, 0))


def your_level(level):
    your_level = font.render("Your level "+str(level), True, (1, 1, 1))
    surface.blit(your_level, (width - your_level.get_rect().right, 20))


class rect_sprite(pygame.sprite.Sprite):
    def __init__(self, rectangle):
        super().__init__()
        self.rect = rectangle


class Point(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.rect = pygame.rect.Rect((0, 0, 20, 20))
        self.rect.center = (random.randint(20, width - 20), random.randint(20, height - 20))

    def draw(self, surface):
        pygame.draw.circle(surface, (0, 0, 255), self.rect.center, 10)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.dir = 0
        self.length = 10
        self.rect = pygame.rect.Rect((width // 2, height // 2, 10, 10))

    def update(self):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[pygame.K_LEFT] and self.dir != 2 and self.dir != 0:
            self.dir = 2
        if pressed_key[pygame.K_RIGHT] and self.dir != 2 and self.dir != 0:
            self.dir = 0
        if pressed_key[pygame.K_UP] and self.dir != 1 and self.dir != 3:
            self.dir = 1
        if pressed_key[pygame.K_DOWN] and self.dir != 1 and self.dir != 3:
            self.dir = 3

    def move(self):
        if 0 < self.rect.center[0] < width and 0 < self.rect.center[1] < height:
            if self.dir == 0:
                self.rect.move_ip(1, 0)
            if self.dir == 1:
                self.rect.move_ip(0, -1)
            if self.dir == 2:
                self.rect.move_ip(-1, 0)
            if self.dir == 3:
                self.rect.move_ip(0, 1)
        if self.rect.center[0] == 0:
            self.rect.center = (width - 1, self.rect.center[1])
        if self.rect.center[0] == width:
            self.rect.center = (1, self.rect.center[1])
        if self.rect.center[1] == 0:
            self.rect.center = (self.rect.center[0], height - 1)
        if self.rect.center[1] == height:
            self.rect.center = (self.rect.center[0], 1)

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 0, 0), self.rect)


Level_random = level_module.Level_creator()
for wall_num in range(random.randint(0, 2)):
    Level_random.rectangles_adder(random.randint(0, width), random.randint(0, height), random.randint(0, width), 5)
    Level_random.rectangles_adder(random.randint(0, width), random.randint(0, height), 5, random.randint(0, height))


my_snake = Player()
point = Point()
all_sprites = pygame.sprite.Group()
all_sprites.add(point)
all_sprites.add(my_snake)
points = pygame.sprite.Group()
points.add(point)
wall_sprite = pygame.sprite.Group()

for rect in Level_random.rect_list:
    rectangle = rect_sprite(rect)
    wall_sprite.add(rectangle)


surface = pygame.display.set_mode((500, 500))

done = False

while not done:
    for event in pygame.event.get():
        print(my_snake.rect.center, my_snake.dir)
        if event.type == pygame.QUIT:
            done = True
        if score % 3 != 0:
            marker = True
    surface.fill((255, 255, 255))
    Level_random.draw(surface)
    your_score(score)
    your_level(level)
    for entity in all_sprites:
        if entity == my_snake:
            entity.update()
            entity.move()
        entity.draw(surface)
    if pygame.sprite.spritecollideany(my_snake, points):
        point.kill()
        point = Point()
        points.add(point)
        all_sprites.add(point)
        score = score + 1
    if score % 3 == 0 and score > 0 and marker:
        Level_random.rectangle_clear()
        for entity in wall_sprite:
            entity.kill()
        for wall_num in range(random.randint(0, 2)):
            Level_random.rectangles_adder(random.randint(0, width), random.randint(0, height), random.randint(0, width), 5)
            Level_random.rectangles_adder(random.randint(0, width), random.randint(0, height), 5, random.randint(0, height))
        for rect in Level_random.rect_list:
            rectangle = rect_sprite(rect)
            wall_sprite.add(rectangle)
        marker = False
        level = level + 1
    if pygame.sprite.spritecollideany(my_snake, wall_sprite):
        done = True
    pygame.display.update()
    clock.tick(60)
