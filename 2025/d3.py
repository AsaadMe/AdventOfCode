with open("input.txt") as file:
    banks = [list(map(int, line.strip())) for line in file.readlines()]


def get_max_joltage1(bank):
    max_jolt = 0
    for i in range(len(bank)):
        for j in range(len(bank)):
            if i < j and (mj := int(str(bank[i]) + str(bank[j]))) > max_jolt:
                max_jolt = mj
    return max_jolt


def get_max_joltage2(bank):
    i = 0
    t = 0
    picked = [None] * 12
    while None in picked:
        max_j = 0
        tt = 0
        for j in range(t, t + len(bank) + 2 - (t + 1) - len([p for p in picked if p is None])):
            if bank[j] > max_j:
                max_j = bank[j]
                tt = j + 1
        picked[i] = max_j
        i += 1
        t = tt

    return int("".join(map(str, picked)))


max_joltages1 = []
for bank in banks:
    max_joltages1.append(get_max_joltage1(bank))

max_joltages2 = []
for bank in banks:
    max_joltages2.append(get_max_joltage2(bank))

print("Part1:", sum(max_joltages1))
print("Part2:", sum(max_joltages2))
