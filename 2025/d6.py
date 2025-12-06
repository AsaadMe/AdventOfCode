from math import prod

with open("input.txt") as file:
    input = file.readlines()

numbers = [list(map(int, line.split())) for line in input[:-1]]
ops = input[-1].split()

ans1 = 0
ops_map = {"+": sum, "*": prod}
for col in range(len(numbers[0])):
    col_values = [numbers[row][col] for row in range(len(numbers))]
    ans1 += ops_map[ops[col]](col_values)

print("Part1:", ans1)

with open("input.txt") as file:
    input = file.readlines()

numbers = [line.rstrip("\n") + " " for line in input[:-1]]
ops = input[-1] + " "
col_lenght = len(ops)

ans2 = 0
ind = 0
nums = []
operation = None
while ind < col_lenght:
    if ops[ind] == "*":
        operation = prod
    elif ops[ind] == "+":
        operation = sum
    elif all([numbers[row][ind] == " " for row in range(len(numbers))]):
        ans2 += operation(nums)
        nums = []
        ind += 1
        continue

    nums.append(int("".join([numbers[row][ind] if numbers[row][ind] != " " else "" for row in range(len(numbers))])))
    ind += 1

print("Part2:", ans2)
