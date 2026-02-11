"""
Docstring for grid draw with pygame
"""

import pygame

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
    
    print(grid_coordinates.__len__())

    row_value = 8
    column_value = 8

    pygame.draw.rect(sample_surface, (255, 0, 0), pygame.Rect(grid_coordinates[column_value - 1][0], grid_coordinates[row_value - 1][0], cell_width, cell_height))
    

    
    #pygame.Rect.move_ip(grid_coordinates[0], 10, 10)


#color = (255,255,255)

#pygame.draw.rect(sample_surface, color, pygame.Rect(30, 30, 60, 60))

x = 1
while True:
    draw_grid(sample_surface, size)
    pygame.display.flip()
    x = x - 0
    if x == 0:
        break
    else:
        pass
    
