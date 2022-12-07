import heapq
elves = []

with open("input.txt") as infile:
    current_elf = 0
    for line in infile:
        if line != '\n':
            current_elf = current_elf + int(line.strip())
        else:
            # boundary - reset state
            elves.append(current_elf)
            current_elf = 0
            continue

print(f"Part 1: {max(elves)}")
print(f"Part 2: {sum(heapq.nlargest(3, elves))}")
