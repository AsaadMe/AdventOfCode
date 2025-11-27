with open("input.txt") as file:
    triangles1 = [list(map(int, line.split())) for line in file.readlines()]

with open("input.txt") as file:
    triangles2 = []
    t1, t2, t3 = [], [], []
    for line in file.readlines():
        a, b, c = map(int, line.split())
        t1.append(a)
        t2.append(b)
        t3.append(c)
        if len(t1) == 3:
            triangles2.append(t1)
            triangles2.append(t2)
            triangles2.append(t3)
            t1, t2, t3 = [], [], []


def count_valid_triangles(triangles):
    valid_triangles = 0
    for triangle in triangles:
        a, b, c = sorted(triangle)
        if a + b > c:
            valid_triangles += 1

    return valid_triangles


print("Part1:", count_valid_triangles(triangles1))
print("Part2:", count_valid_triangles(triangles2))
