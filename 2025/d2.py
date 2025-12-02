import re

with open("input.txt") as file:
    inp = file.readline()


ranges = [a.split("-") for a in inp.split(",")]


def is_invalid_id1(id: str):
    id = id.lstrip("0")
    if len(id) % 2 != 0:
        return False

    mid = len(id) // 2
    if id[:mid] == id[mid:]:
        return True

    return False


def is_invalid_id2(id: str):
    id = id.lstrip("0")
    if re.fullmatch(r"(\d+?)\1+", id):
        return True


ans1 = 0
ans2 = 0
for a, b in ranges:
    for i in range(int(a), int(b) + 1):
        if is_invalid_id1(str(i)):
            ans1 += i
        if is_invalid_id2(str(i)):
            ans2 += i

print("Part1:", ans1)
print("Part2:", ans2)
