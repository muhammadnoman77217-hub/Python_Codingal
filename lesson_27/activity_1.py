import pygame

pygame.init()

screen = pygame.display.set_mode((400,500))

playing = True
while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False


    pygame.display.flip()

pygame.quit()