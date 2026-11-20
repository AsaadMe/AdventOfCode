from functools import cache

tree = {}

with open("input.txt") as f:
    for line in f:
        v1, v2 = line.split(": ")
        tree[v1] = v2.split()


@cache
def part1(v):
    if v == "out":
        return 1

    ans = 0
    for v2 in tree[v]:
        ans += part1(v2)

    return ans


@cache
def part2(v, visited_dac, visited_fft):
    if v == "out":
        if visited_dac and visited_fft:
            return 1
        else:
            return 0

    ans = 0
    for v2 in tree[v]:
        if v == "dac":
            ans += part2(v2, True, visited_fft)
        elif v == "fft":
            ans += part2(v2, visited_dac, True)
        else:
            ans += part2(v2, visited_dac, visited_fft)

    return ans


print("Part1: ", part1("you"))
print("Part2: ", part2("svr", False, False))
