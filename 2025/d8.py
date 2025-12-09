import math
from itertools import combinations

with open("input.txt") as file:
    jboxes = [tuple(map(int, line.strip().split(","))) for line in file.readlines()]


dists = {}
for (x1, y1, z1), (x2, y2, z2) in combinations(jboxes, 2):
    dists[((x1, y1, z1), (x2, y2, z2))] = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)

sorted_dists = sorted(dists.items(), key=lambda x: x[1])

point_to_circuit = {pt: {pt} for pt in jboxes}
iteration = 0
while True:
    (jbox1, jbox2), _ = sorted_dists.pop(0)
    circuit1 = point_to_circuit[jbox1]
    circuit2 = point_to_circuit[jbox2]

    if circuit1 is not circuit2:
        circuit1.update(circuit2)

        for pt in circuit2:
            point_to_circuit[pt] = circuit1

    circuits = {frozenset(s) for s in point_to_circuit.values()}
    sizes = sorted([len(c) for c in circuits], reverse=True)
    iteration += 1

    if iteration == 1000:
        print("Part1:", math.prod(sizes[:3]))

    if len(sizes) == 1:
        print("Part2:", jbox1[0] * jbox2[0])
        break
