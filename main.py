import pygame
#initialize pygame
import pygame.display
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)
# Define constants for the screen width and height
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000

x = pygame.init()
#create screen
screen = pygame.display.set_mode((1000,1000))
#player
playerImg = pygame.image.load('images/pp.png')
playerX = 500
playerY = 800
pygame.display.set_caption('Plane Simulator')
#player display function
def player(playerX , playerY):
    scaled = pygame.transform.scale(playerImg, (150, 150))
    screen.blit(scaled, (playerX, playerY))
 # main loop
running = True
while running:
    player(playerX , playerY)
    for event in pygame.event.get():
        print(event)
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key == pygame.K_UP:
                playerY -= 0.3
    pygame.display.update()











