import string
from typing import List

def to_priority(c: str) -> int:
    """
    Calculates the priority
    """
    priority = 0
    if c.isupper():
        priority = priority + 26
        c = c.lower()
    priority = priority + (string.ascii_lowercase.index(c) + 1)
    return priority

def handle_line_part1(s: str) -> int:
    """
    return the priority value
    """
    line_midpoint = int(len(s) / 2)
    compartment_1 = s[:line_midpoint]
    compartment_2 = s[line_midpoint:]
    print(f"1:{len(compartment_1)} 2:{len(compartment_2)}")
    common = set(compartment_1).intersection(compartment_2)
    print(common)
    return to_priority(common.pop())


def handle_3_lines_part2(s: List[str]) -> int:
    common = set(s[0]).intersection(s[1])
    common = common.intersection(s[2])
    return to_priority(common.pop())


total_priority_1 = 0
total_priority_2 = 0
with open("input") as infile:

    set_3 = []
    for l in infile:
        line = l.strip()
        total_priority_1  = total_priority_1 + handle_line_part1(line)

        # Build the set of 3 for part 2
        set_3.append(line)
        if len(set_3) == 3:
            total_priority_2 = total_priority_2 + handle_3_lines_part2(set_3)
            set_3 = []


print(f"Total (Part 1): {total_priority_1}")
print(f"Total (Part 2): {total_priority_2}")