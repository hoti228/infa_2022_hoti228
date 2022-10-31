import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))
screen.fill((255,255,255))

color = (255, 255, 0) #yellow
circle(screen, color, (200, 175), 100)

color = (255, 0, 0)   #red
circle(screen, color, (150, 150), 20)
circle(screen, color, (250, 150), 15)

color = (0,0,0)       #black
circle(screen, color, (150, 150), 8)
circle(screen, color, (250, 150), 7)
circle(screen, color, (200, 175), 100,1)

rect(screen, color, (150, 225, 100, 20), 10)
pygame.draw.polygon(screen, color,[[100, 90],[175, 145], [175, 135],[100, 80]])
pygame.draw.polygon(screen, color,[[300, 95],[225, 150], [225, 140],[300, 85]])



pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()