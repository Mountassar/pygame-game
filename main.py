import pygame, sys
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

pygame.init()
# create screen
screen = pygame.display.set_mode((1000,1000))
# player
playerX = 500
playerY = 800
pygame.display.set_caption('Plane Simulator')
playerImg = pygame.image.load('images/pp.png')
#player display function
#create second surface
surface_2 = pygame.Surface([playerX,playerY])
def player(playerX , playerY):

    scaled = pygame.transform.scale(playerImg, (500, 400))
    screen.blit (scaled, (playerX, playerY))
clock = pygame.time.Clock()
 # main loop
running = True
while running:
    player(playerX , playerY)
    screen.blit(surface_2, (playerX,playerY))

    for event in pygame.event.get():
        print(id(event.type))
        if event.type == QUIT:
            running = False

        if event.type == KEYDOWN:
            if event.key == K_UP:
                playerY -= 10
                player(playerX, playerY)











