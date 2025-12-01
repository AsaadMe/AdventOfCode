with open("input.txt") as file:
    lines = [line.strip() for line in file.readlines()]

cur_pos = 50
password1 = 0
password2 = 0

for line in lines:
    dir, steps = line[0], int(line[1:])
    if dir == "R":
        password2 += (cur_pos + steps) // 100
        cur_pos = (cur_pos + steps) % 100
    elif dir == "L":
        password2 += steps // 100
        if 1 <= cur_pos <= steps % 100:
            password2 += 1
        cur_pos = (cur_pos - steps) % 100

    if cur_pos == 0:
        password1 += 1

print("Part1:", password1)
print("Part2:", password2)
