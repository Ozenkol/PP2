import time
import title
import pygame
import random
import level_module
import snakedatabase

pygame.init()

# system_variables
marker = True
start_tick = pygame.time.get_ticks()
pygame.mixer.music.load("src/main_menu.mp3")
pygame.mixer.music.play()
width = 500
height = 500
score = 0
level = 1
N = 3
M = 1
deadline = pygame.time.Clock()
clock = pygame.time.Clock()


class rect_sprite(pygame.sprite.Sprite):
    def __init__(self, rectangle):
        super().__init__()
        self.rect = rectangle


class Point(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.weight = random.randint(1, 5)
        self.rect = pygame.rect.Rect((0, 0, 20, 20))
        self.rect.center = (random.randint(20, width - 20), random.randint(20, height - 20))

    def draw(self, surface):
        pygame.draw.circle(surface, (0, 0, 255), self.rect.center, 10)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.speed = 1
        self.unit_num = 0
        self.x_head = width // 2
        self.y_head = height // 2
        self.dir = 0
        self.x = width // 2
        self.y = height // 2
        self.rect = pygame.rect.Rect((self.x, self.y, 10, 10))
        self.rect_dir_list = []
        self.rotate_pos_dir = []

    def update(self):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[pygame.K_LEFT] and self.dir != 2 and self.dir != 0:
            self.dir = 2
            self.rotate_pos_dir.append([[self.rect.x, self.rect.y], 2])
        if pressed_key[pygame.K_RIGHT] and self.dir != 2 and self.dir != 0:
            self.dir = 0
            self.rotate_pos_dir.append([[self.rect.x, self.rect.y], 0])
        if pressed_key[pygame.K_UP] and self.dir != 1 and self.dir != 3:
            self.dir = 1
            self.rotate_pos_dir.append([[self.rect.x, self.rect.y], 1])
        if pressed_key[pygame.K_DOWN] and self.dir != 1 and self.dir != 3:
            self.dir = 3
            self.rotate_pos_dir.append([[self.rect.x, self.rect.y], 3])
        if len(self.rect_dir_list) != 0:
            if self.rotate_pos_dir[0][0] == self.rect_dir_list[0][0].x and self.rotate_pos_dir[0][1] == self.rect_dir_list[0][0].y:
                self.rotate_pos_dir.pop(0)

    def move(self):
        if 0 < self.rect.center[0] < width and 0 < self.rect.center[1] < height:
            if self.dir == 0:
                self.rect.move_ip(self.speed, 0)
            if self.dir == 1:
                self.rect.move_ip(0, -self.speed)
            if self.dir == 2:
                self.rect.move_ip(-self.speed, 0)
            if self.dir == 3:
                self.rect.move_ip(0, self.speed)
            if self.rect.center[0] == 0:
                self.rect.center = (width - 1, self.rect.center[1])
            if self.rect.center[0] == width:
                self.rect.center = (1, self.rect.center[1])
            if self.rect.center[1] == 0:
                self.rect.center = (self.rect.center[0], height - 1)
            if self.rect.center[1] == height:
                self.rect.center = (self.rect.center[0], 1)
        for rect_dir in self.rect_dir_list:
            if rect_dir[1] == 0:
                rect_dir[0].move_ip(self.speed, 0)
            if rect_dir[1] == 1:
                rect_dir[0].move_ip(0, -self.speed)
            if rect_dir[1] == 2:
                rect_dir[0].move_ip(-self.speed, 0)
            if rect_dir[1] == 3:
                rect_dir[0].move_ip(0, self.speed)
            if rect_dir[0].center[0] == 0:
                rect_dir[0].center = (width - 1, rect_dir[0].center[1])
            if rect_dir[0].center[0] == width:
                rect_dir[0].center = (1, rect_dir[0].center[1])
            if rect_dir[0].center[1] == 0:
                rect_dir[0].center = (rect_dir[0].center[0], height - 1)
            if rect_dir[0].center[1] == height:
                rect_dir[0].center = (rect_dir[0].center[0], 1)
            for pos_dir in self.rotate_pos_dir:
                if rect_dir[0].x == pos_dir[0][0] and rect_dir[0].y == pos_dir[0][1]:
                    rect_dir[1] = pos_dir[1]

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 0, 0), self.rect)
        for rect_dir in self.rect_dir_list:
            pygame.draw.rect(surface, (255, 0, 0), rect_dir[0])


Level = 1
speed = 1
marker_for_music = True
main_menu = level_module.Main_menu(None)
save_button = level_module.save_button()
my_score = title.your_score(score)
my_level = title.your_level(Level)
save_title = title.save_title()
my_snake = Player()
point = Point()
all_sprites = pygame.sprite.Group()
all_sprites.add(point)
all_sprites.add(my_snake)
points = pygame.sprite.Group()
points.add(point)
Levels = level_module.Levels(Level, width, height)
wall_sprite = Levels.wall_sprite()
units_sprite = pygame.sprite.Group()


surface = pygame.display.set_mode((500, 500))
main_menu.surface = surface

done = False

while not done:
    event_list = pygame.event.get()
    pygame.mixer.music.set_volume(0.1)
    for event in event_list:
        if event.type == pygame.QUIT:
            done = True
        if score // N > 1:
            marker = True
        if main_menu.active:
            main_menu.update(event)
            main_menu.draw()
    if not main_menu.active and marker_for_music:
        pygame.mixer.music.stop()
        pygame.mixer.music.load("src/snake_theme.mp3")
        pygame.mixer.music.play()
        marker_for_music = False
    if not main_menu.active:
        current_tick = pygame.time.get_ticks()
        seconds = (current_tick - start_tick)/1000
        surface.fill((255, 255, 255))
        Levels.return_level().draw(surface)
        if score // N > 1 and score > 0 and marker:
            for entity in wall_sprite:
                entity.kill()
            Level = Level + 1
            Levels.Level = Level
            speed = speed + 0.25
            my_snake.speed = speed
            for rect in Levels.return_level().rect_list:
                rect_s = rect_sprite(rect)
                wall_sprite.add(rect_s)
            marker = False
            N = N + 3
        if seconds / 5 > M:
            point.kill()
            point = Point()
            points.add(point)
            all_sprites.add(point)
            M = M + 1
        for entity in all_sprites:
            if entity == my_snake:
                entity.update()
                entity.move()
            entity.draw(surface)
        if pygame.sprite.spritecollideany(my_snake, points):
            pygame.mixer.Sound("src/nom_nom.mp3").play()
            if len(my_snake.rect_dir_list) != 0:
                if my_snake.rect_dir_list[-1][1] == 0:
                    pos_x = my_snake.rect_dir_list[-1][0].x - 10
                    pos_y = my_snake.rect_dir_list[-1][0].y
                if my_snake.rect_dir_list[-1][1] == 1:
                    pos_x = my_snake.rect_dir_list[-1][0].x
                    pos_y = my_snake.rect_dir_list[-1][0].y + 10
                if my_snake.rect_dir_list[-1][1] == 2:
                    pos_x = my_snake.rect_dir_list[-1][0].x + 10
                    pos_y = my_snake.rect_dir_list[-1][0].y
                if my_snake.rect_dir_list[-1][1] == 3:
                    pos_x = my_snake.rect_dir_list[-1][0].x
                    pos_y = my_snake.rect_dir_list[-1][0].y - 10
                my_snake.rect_dir_list.append([pygame.rect.Rect(pos_x, pos_y, 10, 10), my_snake.rect_dir_list[-1][1]])
                rect_unit = rect_sprite(my_snake.rect_dir_list[-1][0])
                units_sprite.add(rect_unit)
            else:
                if my_snake.dir == 0:
                    pos_x = my_snake.rect.x - 10
                    pos_y = my_snake.rect.y
                if my_snake.dir == 1:
                    pos_x = my_snake.rect.x
                    pos_y = my_snake.rect.y + 10
                if my_snake.dir == 2:
                    pos_x = my_snake.rect.x + 10
                    pos_y = my_snake.rect.y
                if my_snake.dir == 3:
                    pos_x = my_snake.rect.x
                    pos_y = my_snake.rect.y - 10
                my_snake.rect_dir_list.append([pygame.rect.Rect(pos_x, pos_y, 10, 10), my_snake.dir])
            score = score + point.weight
            point.kill()
            point = Point()
            points.add(point)
            all_sprites.add(point)
            start_tick = pygame.time.get_ticks()
        if pygame.sprite.spritecollideany(my_snake, wall_sprite) or pygame.sprite.spritecollideany(my_snake, units_sprite):
            pygame.mixer.Sound("src/hit.mp3").play()
            time.sleep(1)
            done = True
        if save_button.button.clicked and main_menu.id is not None:
            snakedatabase.insert_scores(main_menu.id, score, level, speed)
            print(snakedatabase.get_scores_by_id(main_menu.id))
            done = True
        save_button.draw(surface)
        my_score.update(score)
        my_level.update(Level)
        my_score.title.draw(surface)
        my_level.title.draw(surface)
        save_title.title.draw(surface)
        save_button.update(event_list)
        pygame.display.update()
        clock.tick(60)
