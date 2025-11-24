with open("input.txt") as file:
    lines = file.readlines()


pad1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
pad2 = [
    [None, None, 1, None, None],
    [None, 2, 3, 4, None],
    [5, 6, 7, 8, 9],
    [None, "A", "B", "C", None],
    [None, None, "D", None, None],
]


def solve(lines, curpos, pad, part):
    ans = ""

    for line in lines:
        for inst in line:
            if inst == "U" and curpos[0] > 0 and pad[curpos[0] - 1][curpos[1]] is not None:
                curpos = (curpos[0] - 1, curpos[1])
            elif inst == "D" and curpos[0] < len(pad) - 1 and pad[curpos[0] + 1][curpos[1]] is not None:
                curpos = (curpos[0] + 1, curpos[1])
            elif inst == "L" and curpos[1] > 0 and pad[curpos[0]][curpos[1] - 1] is not None:
                curpos = (curpos[0], curpos[1] - 1)
            elif inst == "R" and curpos[1] < len(pad[curpos[0]]) - 1 and pad[curpos[0]][curpos[1] + 1] is not None:
                curpos = (curpos[0], curpos[1] + 1)

        ans += str(pad[curpos[0]][curpos[1]])

    print(part, ans)


solve(lines, (1, 1), pad1, "Part 1:")
solve(lines, (2, 0), pad2, "Part 2:")
