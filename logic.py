"""
logic docstring
"""

from tie_break import roth
import itertools
from config import headless_option, size
if headless_option == "0":
    from config import sample_surface



def grid_logic(size, grid_coordinates=False):

    grid = set(itertools.product(range(size), range(size)))

    if grid_coordinates != False:
        usedmoves = move_logic(grid, grid_coordinates)
    else:
        usedmoves = move_logic(grid, grid_coordinates=False, headless=True)
    return usedmoves


def move_logic(grid, grid_coordinates=False, headless=False):

    knight_moves = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]
    valid_moves = []
    used_moves = set() # used moves stored in a set for O(1) lookup
    warns_move = []
    tied_moves = 0
    random_tied_moves_increment = 0
    
    # starting point
    start = (0,0)

    used_moves.add(start)
    point = start

    if (headless == True):
        pass
    else:
        from draw import draw_pattern
        draw_pattern(sample_surface, size, start, grid_coordinates)

    # find valid moves

    print("solving...")

    x = 1
    while True:
        for move in knight_moves:
            new_x = point[0] + move[0]
            new_y = point[1] + move[1]
            if (new_x, new_y) in grid and (new_x, new_y) not in used_moves:
                valid_moves.append((new_x, new_y))

        if not valid_moves: # no more valid moves

            print("\nEnding tour...")

            # stat formatting
            
            stat_moves_total = len(grid)
            stat_moves_made = len(used_moves)
            stat_success_rate = stat_moves_made/stat_moves_total * 100
            stat_tied_moves = tied_moves
            stat_random_tied_moves = random_tied_moves_increment
            stat_percentage_tied_moves = tied_moves/stat_moves_made * 100

            # stats start

            print("Statistics:")
            print(f"Total moves: {stat_moves_total}")
            print(f"Moves made: {stat_moves_made}")
            print(f"Success rate: {stat_success_rate:.2f}%")
            print(f"Tied moves: {stat_tied_moves}")
            print(f"Randomly tie broken: {stat_random_tied_moves}")
            print(f"Percentage of tied moves: {stat_percentage_tied_moves:.2f}%")

            # stats end

            break

        j = 0
        
        # basic warnsdorff implementation
        
        tie_list = []

        if len(valid_moves) >= 1:
            
            # move with least onward moves

            for i in valid_moves:
                y = 0
                for move in knight_moves:
                    new_x = i[0] + move[0]
                    new_y = i[1] + move[1]
                    if (new_x, new_y) in grid and (new_x, new_y) not in used_moves:
                        y = y + 1

                if j == 0:
                    j = y
                    warns_move = i
                elif y < j:
                    tie_list.clear()
                    tie_list.append(i)
                    j = y
                    warns_move = i
                elif y == j:
                    tie_list.append(i)
        else:
            warns_move = valid_moves[0]
            
        # heuristic ending

        if len(tie_list) > 1:
            warns_move, random_value = roth(tie_list, size)
            tied_moves += 1
            if random_value == 1:
                random_tied_moves_increment += 1

        tie_list.clear()

        valid_moves.clear()
        point = warns_move

        #print(warns_move)
        used_moves.add(warns_move)


        if (headless == True):
            pass
        else:
            from draw import draw_pattern
            draw_pattern(sample_surface, size, warns_move, grid_coordinates)


        



        

        



        