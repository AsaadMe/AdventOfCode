with open("input.txt") as file:
    insts = file.readline().split(", ")

cur_pos = (0, 0)
cur_dir = 0  # 0:N, 1:E, 2:S, 3:W
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # N, E, S, W
visited = set()
visited.add(cur_pos)
part2_done = False


for inst in insts:
    turn = inst[0]
    dist = int(inst[1:])

    cur_dir = (cur_dir + (1 if turn == "R" else -1)) % 4

    for _ in range(dist):
        cur_pos = (cur_pos[0] + dirs[cur_dir][0], cur_pos[1] + dirs[cur_dir][1])
        if not part2_done:
            if cur_pos in visited:
                print("Part 2:", abs(cur_pos[0]) + abs(cur_pos[1]))
                part2_done = True
            visited.add(cur_pos)


print("Part 1:", abs(cur_pos[0]) + abs(cur_pos[1]))
