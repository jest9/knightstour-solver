"""
Docstring for init
"""

from config import f, size
from logic import grid_logic
from grid import draw_grid

print("welcome to knightstour")

print(f)

if f == 1:
    grid_logic(size)

elif f == 0:
    from config import sample_surface
    draw_grid(sample_surface, size)




