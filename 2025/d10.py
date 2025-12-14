from collections import Counter
from functools import cache
from itertools import combinations

with open("input.txt") as file:
    inp = [line.strip() for line in file.readlines()]


@cache
def run(buttons, schematic, req):
    j = [0] * len(req)
    buttons = {a: b for a, b in buttons}
    for b, c in buttons.items():
        for i in b:
            j[i] += c
    j = tuple(j)

    if j == req:
        return sum(buttons.values())

    if any([a > b for a, b in zip(j, req)]):
        return float("inf")

    branches = []
    for sc in schematic:
        nxbuttons = buttons.copy()
        if sc in buttons:
            nxbuttons[sc] += 1
        else:
            nxbuttons[sc] = 1
        nxbuttons = tuple(sorted(nxbuttons.items()))
        branches.append(run(nxbuttons, schematic, req))

    return min(branches)


ans1 = 0
ans2 = 0
for machine in inp:
    finded1 = False
    diagram, *schematics, joltage_reqs = machine.split()
    diagram = diagram[1:-1]
    joltage_reqs = joltage_reqs[1:-1]

    for r in range(1, len(schematics) + 1):
        if not finded1:
            for combo in combinations(schematics, r):
                combo_diagram = ""
                counter = Counter("".join(combo))

                for i in range(len(diagram)):
                    if counter.get(str(i), 0) % 2 == 0:
                        combo_diagram += "."
                    else:
                        combo_diagram += "#"

                if diagram == combo_diagram:
                    ans1 += r
                    finded1 = True
                    break

    schematics = tuple([eval(sc) if isinstance(eval(sc), tuple) else (eval(sc),) for sc in schematics])
    joltage_reqs = tuple(map(int, joltage_reqs.split(",")))
    # ans2 += run((), schematics, joltage_reqs)
    # run.cache_clear()

print("Part1:", ans1)
print("Part2:", ans2)
