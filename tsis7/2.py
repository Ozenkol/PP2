import pygame

pygame.init()
pygame.font.init()


SONG_END = pygame.USEREVENT + 1
pygame.mixer.music.set_endevent(SONG_END)
pos = 0
playlist = ["src/bad_apple.mp3", "src/bad_apple_remix_1.mp3", "src/because_princess.mp3"]
is_pause = False
vol = 1.0

HEIGHT = 400
WIDTH = 400
my_font = pygame.font.SysFont("src/comicsansms", 30)
my_text_1 = my_font.render("Press 'S' to stop playlist", False, (0, 0, 0))
my_text_2 = my_font.render("Press 'R' to run playlist", False, (0, 0, 0))
my_text_3 = my_font.render("Press 'P' to pause/unpause playlist", False, (0, 0, 0))
my_text_4 = my_font.render("Press '<- ->' to play prev/next music", False, (0, 0, 0))
my_text_5 = my_font.render("Press 'UP/DOWN' to regulate volume", False, (0, 0, 0))


clock = pygame.time.Clock()
surface = pygame.display.set_mode((HEIGHT, WIDTH))
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                if not is_pause:
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
                is_pause = not is_pause
            elif event.key == pygame.K_s:
                pygame.mixer.music.stop()
            elif event.key == pygame.K_r:
                pygame.mixer.music.load(playlist[0])
                pygame.mixer.music.play()
            elif event.key == pygame.K_DOWN:
                vol -= 0.1
                pygame.mixer.music.set_volume(vol)
            elif event.key == pygame.K_UP:
                vol += 0.1
                pygame.mixer.music.set_volume(vol)
            elif event.key == pygame.K_RIGHT:
                pos += 1
                pygame.mixer.music.load(playlist[abs(pos) % len(playlist)])
                pygame.mixer.music.play()
            elif event.key == pygame.K_LEFT:
                pos -= 1
                pygame.mixer.music.load(playlist[abs(pos) % len(playlist)])
                pygame.mixer.music.play()
        if event.type == SONG_END:
            pos += 1
            pygame.mixer.music.load(playlist[abs(pos) % len(playlist)])
            pygame.mixer.music.play()

    surface.fill((255, 255, 255))
    surface.blit(my_text_1, (0, 0))
    surface.blit(my_text_2, (0, 40))
    surface.blit(my_text_3, (0, 70))
    surface.blit(my_text_4, (0, 100))
    surface.blit(my_text_5, (0, 130))

    clock.tick(60)
    pygame.display.flip()
