
import pygame

def draw_pattern(surface, size, value, grid_coordinates):

    width, height = surface.get_size()
    cell_width = width // size  # calculates width and height of each cell
    cell_height = height // size

    row_value = 1
    column_value = 1

    (x, y) = value

    row_value = x
    column_value = y

    pygame.draw.rect(surface, (173, 216, 230), pygame.Rect(grid_coordinates[column_value][0], grid_coordinates[row_value][0], cell_width, cell_height))
        
    pygame.display.flip()
    pygame.event.pump()
