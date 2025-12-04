grid_papers = set()

with open("input.txt") as file:
    for i, line in enumerate(file):
        for j, char in enumerate(line.strip()):
            if char == "@":
                grid_papers.add((i, j))


def get_accessible_papers(grid):
    adjs = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

    accessible_papers = set()
    for paperx, papery in grid:
        adj_count = 0
        for x, y in adjs:
            if (paperx + x, papery + y) in grid:
                adj_count += 1
        if adj_count < 4:
            accessible_papers.add((paperx, papery))
    return accessible_papers


print("Part1:", len(get_accessible_papers(grid_papers)))

removed = 0
while True:
    accessible_papers = get_accessible_papers(grid_papers)
    removed += len(accessible_papers)
    if len(accessible_papers) == 0:
        break
    for paper in accessible_papers:
        grid_papers.remove(paper)

print("Part2:", removed)
