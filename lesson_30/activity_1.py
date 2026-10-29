import math
import random
import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500
PLAYER_START_X = 370
PLAYER_START_Y = 380
ENEMY_START_Y_MIN = 50
ENEMY_START_Y_MIX_ = 150
ENEMY_SPEED_X = 4
ENEMY_SPEED_Y = 40
BULLET_SPEED_WHY = 10
COLLISSION_DISTANCE = 27

pygame.init()
screen = pygame.discplay.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

background=pygame.image.load(('background.jpg' ))
pygame.display.set_caption("Space Invader")
icon = pygame.image.load('ufo.pg')
pygame.display.set_icon(icon)

playerImg = pygame.image.load('rocket.pmg')
playerX = PLAYER_START_X
playerY = PLAYER_START_Y

enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range (num_of_enemies):
    enemyImg.append(pygame.image.load('alien.png'))
    enemyX.append(random.randint(0, SCREEN_WIDTH - 64))
    enemyY.append(random.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MIX_))
    enemyX_change.append(ENEMY_SPEED_X)
    enemyY_change.append(ENEMY_SPEED_Y)

bulletImg = pygame.image.load('bullet.png')
bulletY = 0
bulletX = PLAYER_START_Y
bulletY_change = BULLET_SPEED_Y
bullet_state = "ready"

score_value = 0
font = pygame.font.font('freesansbold.ttf', 32)
textX = 10
textY = 10

over_font = pygame.font.font('freesansbold.tff', 64)