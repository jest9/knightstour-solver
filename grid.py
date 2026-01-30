"""
Docstring for grid draw with pygame
"""

import pygame

print("gridding up....")

pygame.init()

sample_surface = pygame.display.set_mode((400,400))

#color = (255,255,255)

#pygame.draw.rect(sample_surface, color, pygame.Rect(30, 30, 60, 60))

x = 1
while True:
    pygame.display.flip()
    x = x +0
    if x == 0:
        break
    else:
        pass
    
