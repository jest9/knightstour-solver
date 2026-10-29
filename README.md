<div align="center">

# Knight's Tour Solver

**A pure heuristic solver: Warnsdorff's rule with Roth's tie-break, no backtracking.**

![Solver running on a 200×200 board](gifs/warnsroth200.gif)

</div>

## What it does

A [knight's tour](https://en.wikipedia.org/wiki/Knight%27s_tour) is a sequence of knight moves that visits every square on a board exactly once. This solver finds one on square boards of any size, and can either animate the tour with pygame or run headless for speed.

## How it works

The solver never backtracks. At every step it picks the next square with a rule of thumb:

1. **Warnsdorff's rule:** move to the square that has the fewest onward moves left. Squares that are hard to reach get visited before they become dead ends.
2. **Roth's tie-break:** when several squares tie, pick the one farthest from the centre of the board. Plain Warnsdorff often fails on larger boards because of bad tie choices; this fixes most of them.
3. **Random fallback:** if squares are still tied after that, pick one at random.

Because there's no backtracking, each move costs about the same small amount of work, so the time grows in step with the number of squares.

## Performance

Headless mode, starting from the corner, Python 3.13. Times will vary by machine.

| Board | Squares | Time | Complete tour |
|---|---|---|---|
| 8×8 | 64 | 0.03s | ✓ |
| 100×100 | 10,000 | 0.09s | ✓ |
| 200×200 | 40,000 | 0.29s | ✓ |
| 500×500 | 250,000 | 1.9s | ✓ |
| 1000×1000 | 1,000,000 | 10.2s | ✓ |

Ten runs each at 8×8, 50×50, 300×300 and 500×500 all produced complete tours.

## Running it

Install the dependency (pygame is only needed for visual mode):

```bash
pip install -r requirements.txt
```

Then run:

```bash
python init.py
```

You'll be asked for:

- **Mode:** `0` for visual mode (animated in a pygame window) or `1` for headless mode (no window, runs under `cProfile`)
- **Grid size:** e.g. `8` for a standard chessboard

## Output

When the tour ends, the solver prints some statistics:

```
Statistics:
Total moves: 64
Moves made: 64
Success rate: 100.00%
Tied moves: 13
Randomly tie broken: 3
Percentage of tied moves: 20.31%
```

- **Success rate:** the share of squares visited (100% means a complete tour)
- **Tied moves:** how many times Warnsdorff's rule couldn't decide on its own and Roth's tie-break was needed
- **Randomly tie broken:** how many of those were still tied and had to be settled at random

In headless mode, a `cProfile` breakdown follows, showing where the time went.

## Project structure

| File | Purpose |
|---|---|
| `init.py` | Entry point; starts headless or visual mode |
| `config.py` | Asks for mode and board size, sets up the pygame window |
| `logic.py` | The solver: move generation and Warnsdorff's rule |
| `tie_break.py` | Roth's tie-break with random fallback |
| `stats.py` | Prints the end-of-tour statistics |
| `grid.py` | Draws the board grid (visual mode) |
| `draw.py` | Draws each visited square (visual mode) |

## Limitations

- The tour always starts from the top-left corner.
- It finds an *open* tour (the knight doesn't have to end a move away from where it started).
- As a pure heuristic with no backtracking, it isn't guaranteed to succeed on every board, though it completed every size tested above.

## Ideas for the future

- Divide and conquer for very large boards
- Choosing the starting square
