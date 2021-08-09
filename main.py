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
pygame.get_init()
# create screen
screen = pygame.display.set_mode((1000,1000))
#name caption
pygame.display.set_caption('Plane Simulator')
screen.fill((255,200,200))
# player definition
playerX = 300
playerY = 300
plane = pygame.image.load('images/pp.png')
#create second surface
surface_2 = pygame.Surface((playerX, playerY))
# main loop
running = True
while running:
    screen.fill((255,255,255))
    screen.blit(plane,(playerX,playerY))
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                playerX -= 10
            if event.key == K_RIGHT:
                playerX += 10
            if event.key == K_UP:
                playerY -= 10
            if event.key == K_DOWN:
                playerY += 10
    pygame.display.flip()









