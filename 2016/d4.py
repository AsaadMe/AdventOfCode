from collections import Counter

ans1 = 0
real_names = []

with open("input.txt") as file:
    lines = file.readlines()
    for line in lines:
        parts = line.strip().split("-")
        letters = "".join(parts[:-1])
        sector_id = int(parts[-1].split("[")[0])
        checksum = parts[-1].split("[")[1][:-1]

        letter_counts = Counter(letters)
        letters_sorted = sorted(letter_counts.items(), key=lambda x: (-x[1], x[0]))
        calculated_checksum = "".join([letter for letter, count in letters_sorted[:5]])
        if calculated_checksum == checksum:
            ans1 += sector_id

        name = ""
        for part in parts[:-1]:
            decrypt_part = ""
            for char in part:
                decrypt_part += chr((ord(char) - ord("a") + sector_id) % 26 + ord("a"))

            name += decrypt_part + " "

        real_names.append((name.strip(), sector_id))

print("Part 1:", ans1)
print("Part 2:", [item[1] for item in real_names if "north" in item[0]][0])
