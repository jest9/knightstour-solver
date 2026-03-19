import pygame
import time

def draw_pattern(surface, size, value, grid_coordinates):
    width, height = surface.get_size()
    cell_width = width // size  # calculates width and height of each cell
    cell_height = height // size

    #print(value)

    row_value = 1
    column_value = 1
    
    count = 1
    checker = 1

    #time.sleep(1000000)

    # unpack tuple of moves and draw pattern on grid
    (x, y) = value

    row_value = x
    column_value = y
    # clear cell
    if checker == 1:
        pygame.draw.rect(surface, (0, 0, 0), pygame.Rect(grid_coordinates[column_value][0], grid_coordinates[row_value][0], cell_width, cell_height))
    elif checker == 0:
        pygame.draw.rect(surface, (255, 255, 255), pygame.Rect(grid_coordinates[column_value][0], grid_coordinates[row_value][0], cell_width, cell_height))
        
    # draw number
    font = pygame.font.Font(None, 36)
    if checker == 1:
        text = font.render(str(count), True, (255, 255, 255))
        checker = 0

    elif checker == 0:
        text = font.render(str(count), True, (0, 0, 0))
        checker = 1
        
    text_rect = text.get_rect(center=(grid_coordinates[column_value][0] + cell_width//2, 
                                          grid_coordinates[row_value][0] + cell_height//2))
    surface.blit(text, text_rect)
        
    pygame.display.flip()
    pygame.event.pump()

    time.sleep(0.1)

    count += 1