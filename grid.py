"""
Docstring for grid draw with pygame
"""

import pygame
import time
import logic


print("gridding up....")


# solving logic #

size = int(input("provide grid size: "))


# test for drawing value to visual grid.

value2 = logic.grid_logic(size)

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
            pygame.draw.rect(surface, (255, 255, 255), rect, 1) # draw grid lines
            grid_coordinates.append((j * cell_width, i * cell_height)) # store grid coordinates in list
    
    #print(grid_coordinates.__len__())


def draw_pattern(surface, size, value):
    width, height = surface.get_size()
    cell_width = width // size  # calculates width and height of each cell
    cell_height = height // size

    row_value = 1
    column_value = 1
    colour_value = 255

    
    for x,y in value:
        row_value = x
        column_value = y
        pygame.draw.rect(sample_surface, (0, colour_value, 0), pygame.Rect(grid_coordinates[column_value][0], grid_coordinates[row_value][0], cell_width, cell_height))
        pygame.display.flip()
        time.sleep(1)

    


    #for i in range(size):
    #    pygame.draw.rect(sample_surface, (0, colour_value, 0), pygame.Rect(grid_coordinates[column_value - 1][0], grid_coordinates[row_value - 1][0], cell_width, cell_height))
    #    row_value = row_value + 2
    #    column_value = column_value + 3
    #    colour_value = colour_value - 1
    #    pygame.display.flip()
    #    time.sleep(1)


draw_grid(sample_surface, size)
draw_pattern(sample_surface, size, value2)
    
