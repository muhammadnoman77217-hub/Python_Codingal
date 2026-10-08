import pygame

pygame.init()
SCREEN_WIDTH ,SCREEN_HEIGHT = 500,500

display_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Adding image and background image')

background_image = pygame.image.load('background.jpeg').convert()
background_image = pygame.transform.scale(background_image, (SCREEN_HEIGHT, SCREEN_WIDTH))

Klein_image = pygame.image.load('klein.png').convert_alpha()
Klein_image = pygame.transform.scale(Klein_image, (200, 200))

Klein_rect = Klein_image.get_rect(center=(SCREEN_HEIGHT // 2,SCREEN_HEIGHT // 2 - 30))

