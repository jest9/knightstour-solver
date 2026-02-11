"""
Docstring for grid draw with pygame
"""

import pygame
import time

print("gridding up....")

# grid size # 

size = 8

pygame.init()

sample_surface = pygame.display.set_mode((600,600))

# grid handling

grid_coordinates = [] # for storing grid coordinates

def draw_grid(surface, size):
    width, height = surface.get_size()
    cell_width = width // size  # calculates width and height of each cell
    cell_height = height // size

    for i in range(size):   # loops drawing grid lines
        for j in range(size):
            rect = pygame.Rect(j * cell_width, i * cell_height, cell_width, cell_height)
            pygame.draw.rect(surface, (255, 255, 255), rect, 1) # draw grid lines
            grid_coordinates.append((j * cell_width, i * cell_height)) # store grid coordinates in list
    
    #print(grid_coordinates.__len__())


def draw_pattern(surface, size):
    width, height = surface.get_size()
    cell_width = width // size  # calculates width and height of each cell
    cell_height = height // size

    row_value = 1
    column_value = 1

    for i in range(size):
            pygame.draw.rect(sample_surface, (0, 255, 0), pygame.Rect(grid_coordinates[column_value - 1][0], grid_coordinates[row_value - 1][0], cell_width, cell_height))
            row_value = row_value + 1
            column_value = column_value + 1
            pygame.display.flip()
            time.sleep(1)


draw_grid(sample_surface, size)
draw_pattern(sample_surface, size)
    
