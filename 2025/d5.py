with open("input.txt") as file:
    fresh, ids = file.read().strip().split("\n\n")
    ids = map(int, ids.splitlines())


fresh_ids = [list(map(int, line.split("-"))) for line in fresh.splitlines()]

fresh_count = 0
for id in ids:
    for rangex, rangey in fresh_ids:
        if rangex <= id <= rangey:
            fresh_count += 1
            break

print("part1:", fresh_count)

fresh_ids.sort(key=lambda x: x[0])

final_fresh_ids = []

current_rangex, current_rangey = fresh_ids[0]

for i in range(1, len(fresh_ids)):
    next_rangex, next_rangey = fresh_ids[i]

    if next_rangex <= current_rangey + 1:
        current_rangey = max(current_rangey, next_rangey)
    else:
        final_fresh_ids.append((current_rangex, current_rangey))
        current_rangex, current_rangey = next_rangex, next_rangey

final_fresh_ids.append((current_rangex, current_rangey))

all_fresh_count = 0
for x, y in final_fresh_ids:
    all_fresh_count += y - x + 1

print("Part2:", all_fresh_count)
