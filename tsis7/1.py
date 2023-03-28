import pygame
import datetime

current_second = datetime.datetime.now().second
current_minute = datetime.datetime.now().minute

pygame.init()
mickey_mouse = pygame.image.load("src/mickey.png")
mickey_mouse = pygame.transform.scale(mickey_mouse, (500, 500))
minute_hand = pygame.image.load("src/minute_hand.png")
minute_hand = pygame.transform.scale(minute_hand, (250, 250))
hour_hand = pygame.image.load("src/hour_hand.png")
clock = pygame.time.Clock()
surface = pygame.display.set_mode((500, 500))
done = False
angle = 1

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    surface.fill((255, 255, 255))
    surface.blit(mickey_mouse, (0, 0))
    rotated_minute_hand = pygame.transform.rotozoom(minute_hand, 45-datetime.datetime.now().second*6, 1)
    rotated_hour_hand = pygame.transform.rotozoom(hour_hand, 132-datetime.datetime.now().minute*6, 1)
    rect_minute_hand = rotated_minute_hand.get_rect(center = (250, 250))
    rect_hour_hand = rotated_hour_hand.get_rect(center = (250, 250))
    surface.blit(rotated_hour_hand, rect_hour_hand)
    surface.blit(rotated_minute_hand, rect_minute_hand)
    pygame.display.flip()
    clock.tick(60)
