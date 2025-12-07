from functools import cache

with open("input.txt") as file:
    grid = [list(line.strip()) for line in file.readlines()]

start = (0, grid[0].index("S"))

beams = {(start[0] + 1, start[1])}
grid[start[0] + 1][start[1]] = "|"
splits = 0
while True:
    nxt_grid = [row.copy() for row in grid]

    new_beams = set()
    for x, y in beams:
        if grid[x + 1][y] == ".":
            nxt_grid[x + 1][y] = "|"
            new_beams.add((x + 1, y))
        elif grid[x + 1][y] == "^":
            splits += 1
            if nxt_grid[x + 1][y + 1] != "|":
                nxt_grid[x + 1][y + 1] = "|"
                new_beams.add((x + 1, y + 1))
            if nxt_grid[x + 1][y - 1] != "|":
                nxt_grid[x + 1][y - 1] = "|"
                new_beams.add((x + 1, y - 1))

    if x == len(grid) - 2:
        break

    beams = new_beams
    grid = nxt_grid

print("Part1:", splits)

###############################################################

with open("input.txt") as file:
    grid = [list(line.strip()) for line in file.readlines()]

rows = len(grid)
cols = len(grid[0])

start_col = grid[0].index("S")


@cache
def solve(row, col):
    for nxt_row in range(row + 1, rows):
        if grid[nxt_row][col] == "^":
            total_timelines = solve(nxt_row, col - 1) + solve(nxt_row, col + 1)

            return total_timelines

    return 1


print("Part2:", solve(0, start_col))
