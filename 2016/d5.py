import hashlib


def part1():
    input_string = "cxdnnyjw"
    password = ""
    ind = 0
    while True:
        test_string = input_string + str(ind)
        hash_result = hashlib.md5(test_string.encode("utf-8")).hexdigest()
        if hash_result.startswith("00000"):
            password += hash_result[5]
            if len(password) == 8:
                break
        ind += 1

    print("Part1:", password)


def part2():
    input_string = "cxdnnyjw"
    password = [None] * 8
    ind = 0
    while True:
        test_string = input_string + str(ind)
        hash_result = hashlib.md5(test_string.encode("utf-8")).hexdigest()
        if hash_result.startswith("00000") and hash_result[5] in "01234567":
            pos = int(hash_result[5])
            char = hash_result[6]
            if password[pos] is None:
                password[pos] = char
            if None not in password:
                break
        ind += 1

    print("Part2:", "".join(password))


part1()
part2()
