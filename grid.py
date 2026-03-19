"""
Docstring for grid draw with pygame
"""

import pygame
import time
import logic
import random


print("gridding up....")


# solving logic #

size = int(input("provide grid size: "))

icon_path = "icons/chess.jpeg" # path to chess piece icon for drawing pattern on grid
programIcon = pygame.image.load(icon_path) # load icon image
# test for drawing value to visual grid.

#value2 = logic.grid_logic(size)

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
            pygame.display.set_caption("Knight's Tour") # set window title
            pygame.display.set_icon(programIcon) # set window icon
            grid_coordinates.append((j * cell_width, i * cell_height)) # store grid coordinates in list

    logic.grid_logic(size, surface, grid_coordinates) # call grid logic to get moves and draw pattern on grid


#def draw_pattern(surface, size, value):
#    width, height = surface.get_size()
#    cell_width = width // size  # calculates width and height of each cell
#    cell_height = height // size

    #print(value)

#    row_value = 1
#    column_value = 1
    
#    count = 1
#    checker = 1


#   for x, y in value:
#        row_value = x
#        column_value = y
        # clear cell
#        if checker == 1:
#            pygame.draw.rect(surface, (0, 0, 0), pygame.Rect(grid_coordinates[column_value][0], grid_coordinates[row_value][0], cell_width, cell_height))
#        elif checker == 0:
#            pygame.draw.rect(surface, (255, 255, 255), pygame.Rect(grid_coordinates[column_value][0], grid_coordinates[row_value][0], cell_width, cell_height))
#        
#        # draw number
#        font = pygame.font.Font(None, 36)
#        if checker == 1:
#            text = font.render(str(count), True, (255, 255, 255))
#            checker = 0

#        elif checker == 0:
#            text = font.render(str(count), True, (0, 0, 0))
#            checker = 1
        
#        text_rect = text.get_rect(center=(grid_coordinates[column_value][0] + cell_width//2, 
#                                          grid_coordinates[row_value][0] + cell_height//2))
#        surface.blit(text, text_rect)
#        
#        pygame.display.flip()
#        pygame.event.pump()
#
#        count += 1


#    print("squares filled: ", len(value))
#    time.sleep(1000)


draw_grid(sample_surface, size)
#draw_pattern(sample_surface, size, value2)
    
