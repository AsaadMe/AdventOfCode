with open("input.txt") as file:
    lines = [line.strip() for line in file.readlines()]


count = [{} for _ in range(len(lines[0]))]

for line in lines:
    for i, char in enumerate(line):
        if char not in count[i]:
            count[i][char] = 1
        count[i][char] += 1

print("Part1:", "".join([sorted(dic.items(), key=lambda x: x[1], reverse=True)[0][0] for dic in count]))
print("Part2:", "".join([sorted(dic.items(), key=lambda x: x[1])[0][0] for dic in count]))
