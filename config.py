"""
docstring for config
"""

headless_option = input("Please input 1 for headless mode, or 0 for visual mode: \n")
size = int(input("provide grid size: "))

if headless_option == "0":
    import pygame
    pygame.init
    sample_surface = pygame.display.set_mode((800,800))
    f = 0
else:
    f = 1