"""
Docstring for grid draw with pygame
"""

import pygame
import logic


print("gridding up....")

size = int(input("provide grid size: "))


# setup window and icon

icon_path = "icons/chess.jpeg"
programIcon = pygame.image.load(icon_path)

# grid size # 

pygame.init()

sample_surface = pygame.display.set_mode((800,800))

# grid handling

grid_coordinates = [] # for storing grid coordinates

def draw_grid(surface, size):
    width, height = surface.get_size()
    cell_width = width // size  # calculates width and height of each cell
    cell_height = height // size

    for i in range(size):   # loops drawing grid lines
        for j in range(size):
            rect = pygame.Rect(j * cell_width, i * cell_height, cell_width, cell_height)
            pygame.draw.rect(surface, (255, 255, 255), rect, 1)
            pygame.display.set_caption("Knight's Tour")
            pygame.display.set_icon(programIcon)

            grid_coordinates.append((j * cell_width, i * cell_height)) # store grid coordinates in list

    logic.grid_logic(size, surface, grid_coordinates) # call logic engine


draw_grid(sample_surface, size)

    
