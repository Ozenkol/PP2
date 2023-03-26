import pygame
import datetime

def rotate(image, angle, pivor, offset):
    rotated_image = pygame.transform.rotozoom(image, -angle, 1)
    rotated_offset = offset.rotate(angle)
    rect = rotated_image.get_rect(center=rotated_offset + pivor)
    return  rotated_image, rect

current_minute = datetime.datetime.now().minute
current_hour = datetime.datetime.now().hour

pygame.init()
mickey_mouse = pygame.image.load("src/mickey.png")
mickey_mouse = pygame.transform.scale(mickey_mouse, (500, 500))
minute_hand = pygame.image.load("src/minute_hand.png")
hour_hand = pygame.image.load("src/hour_hand.png")
clock = pygame.time.Clock()
offset_1 = pygame.math.Vector2(55, -50)
offset_2 = pygame.math.Vector2(50, 30)
surface = pygame.display.set_mode((500, 500))
done = False
angle = 1

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    surface.fill((255, 255, 255))
    surface.blit(mickey_mouse, (0, 0))
    rotated_minute_hand, rect_minute_hand = rotate(minute_hand, -54+datetime.datetime.now().minute*6, (250, 250), offset_1) #250 160
    rotated_hour_hand, rect_hour_hand = rotate(hour_hand, -120+(datetime.datetime.now().hour % 12)*30, (250, 250), offset_2) #240 230
    surface.blit(rotated_minute_hand, rect_minute_hand)
    surface.blit(rotated_hour_hand, rect_hour_hand)
    pygame.display.flip()
    clock.tick(60)
