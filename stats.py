"""
docstring for stats for tour
"""

def stats(stat_moves_total, stat_moves_made, stat_tied_moves, stat_random_tied_moves):

    stat_success_rate = stat_moves_made/stat_moves_total * 100
    stat_percentage_tied_moves = stat_tied_moves/stat_moves_made * 100

    print("Statistics:")
    print(f"Total moves: {stat_moves_total}")
    print(f"Moves made: {stat_moves_made}")
    print(f"Success rate: {stat_success_rate:.2f}%")
    print(f"Tied moves: {stat_tied_moves}")
    print(f"Randomly tie broken: {stat_random_tied_moves}")
    print(f"Percentage of tied moves: {stat_percentage_tied_moves:.2f}%")
    print("\033[0m")

    # stats end