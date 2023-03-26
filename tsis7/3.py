import pygame

pygame.init()

HEIGHT = 1000
WIDTH = 500
raduis = 25
surface = pygame.display.set_mode((HEIGHT, WIDTH))
x = raduis
y = raduis
clock = pygame.time.Clock()
done = False
is_pressed = False

while not done:
    pressed = pygame.key.get_pressed()
    for action in pygame.event.get():
        if action.type == pygame.QUIT:
            done = True
        if pressed:
            is_pressed = True
        if is_pressed:
            if pressed[pygame.K_UP] and y >= 25:
                y -= 20
                is_pressed = False
            if pressed[pygame.K_DOWN] and y <= WIDTH - raduis:
                y += 20
                is_pressed = False
            if pressed[pygame.K_LEFT] and x >= 25:
                x -= 20
                is_pressed = False
            if pressed[pygame.K_RIGHT] and x <= HEIGHT - raduis:
                x += 20
                is_pressed = False

    surface.fill((0, 0, 0))
    pygame.draw.circle(surface, (255, 255, 255), (x, y), 25)
    pygame.display.flip()
    clock.tick(60)
