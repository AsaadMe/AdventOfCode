import re

with open("input.txt") as file:
    lines = [line.strip() for line in file.readlines()]


def part1():
    tls_support_count = 0
    tls_pattern = re.compile(r"(.)(?!\1)(.)\2\1")

    for line in lines:
        insides = re.findall(r"\[(.*?)\]", line)
        for inside in insides:
            if re.search(tls_pattern, inside):
                break
        else:
            if re.search(tls_pattern, line):
                tls_support_count += 1

    print("Part1:", tls_support_count)


def part2():
    ssl_support_count = 0

    for line in lines:
        insides = re.findall(r"\[([a-z]+)\]", line)

        outsides = re.split(r"\[[a-z]+\]", line)

        ABA_pattern = r"(?=(.)(?!\1)(.)\1)"
        found_abas = []

        for part in outsides:
            matches = re.findall(ABA_pattern, part)
            found_abas.extend(matches)

        for a, b in found_abas:
            bab = f"{b}{a}{b}"
            if any(bab in part for part in insides):
                ssl_support_count += 1
                break

    print("Part2:", ssl_support_count)


part1()
part2()
