from itertools import combinations

with open("input.txt") as file:
    points = [list(map(int, line.strip().split(","))) for line in file.readlines()]

ans1 = 0
for (x1, y1), (x2, y2) in combinations(points, 2):
    if x1 == x2 or y1 == y2:
        ans1 = max(ans1, abs(x1 - x2) + abs(y1 - y2) + 1)

    else:
        ans1 = max(ans1, abs(x1 - x2 + 1) * abs(y1 - y2 + 1))

print("Part1:", ans1)
