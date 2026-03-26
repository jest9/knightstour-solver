"""
Docstring for init
"""

from config import f, size
from logic import grid_logic

print("\n")

if f == 1:                      # method to decouple the solver from pygame, allows for headless
    grid_logic(size)

elif f == 0:
    from grid import draw_grid
    from config import sample_surface
    draw_grid(sample_surface, size)




