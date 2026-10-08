import pygame

pygame.init()
SCREEN_WIDTH ,SCREEN_HEIGHT = 500,500

display_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Adding image and background image')

background_image = pygame.image.load('E:/Python_Codingal/lesson_27/background.jpeg').convert()
background_image = pygame.transform.scale(background_image, (SCREEN_HEIGHT, SCREEN_WIDTH))

Klein_image = pygame.image.load('E:/Python_Codingal/lesson_27/Klein.png').convert_alpha()
Klein_image = pygame.transform.scale(Klein_image, (200, 200))

Klein_rect = Klein_image.get_rect(center=(SCREEN_HEIGHT // 2,SCREEN_HEIGHT // 2 - 30))

text = pygame.font.Font(None, 36).render('Hello World', True,   pygame.Color('black'))
text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 110))

clock = pygame.time.Clock()
playing = True
while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
    display_surface.blit(background_image, (0, 0))
    display_surface.blit(Klein_image, Klein_rect)
    display_surface.blit(text, text_rect)
    pygame.display.update()
    clock.tick(60)
pygame.quit()