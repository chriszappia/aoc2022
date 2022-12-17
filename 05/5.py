from textwrap import wrap
import re
"""
                    [L]     [H] [W]
                [J] [Z] [J] [Q] [Q]
[S]             [M] [C] [T] [F] [B]
[P]     [H]     [B] [D] [G] [B] [P]
[W]     [L] [D] [D] [J] [W] [T] [C]
[N] [T] [R] [T] [T] [T] [M] [M] [G]
[J] [S] [Q] [S] [Z] [W] [P] [G] [D]
[Z] [G] [V] [V] [Q] [M] [L] [N] [R]
 1   2   3   4   5   6   7   8   9
"""


class Stacks:
    stacks = []

    def __init__(self, stacks):
        self.stacks = stacks
        pass

    def move_boxes_part1(self, count, from_stack, to_stack):
        for i in range(0, count):
            box = self.stacks[from_stack - 1].pop()
            self.stacks[to_stack - 1].append(box)

    def move_boxes_part2(self, count, from_stack, to_stack):
        # Take a slice
        start_index = count * -1
        boxes = self.stacks[from_stack - 1][start_index:]
        # Remove the slice
        self.stacks[from_stack - 1] = self.stacks[from_stack - 1][:start_index]
        # Add the whole slice
        self.stacks[to_stack - 1].extend(boxes)

    def get_stack_tops(self) -> str:
        return "".join([x.pop() for x in self.stacks])


with open("input") as infile:
    stacks = []
    for line in infile:
        # Parse the initial state
        if line.isspace():
            # If the blank line, skip
            # Break because that's the end of the initial state
            break
        if '1' in line:
            # if the numbers skip
            continue

        components = wrap(line, 4, drop_whitespace=False)
        if len(stacks) == 0:
            for i in range(0, len(components)):
                stacks.append([])

        for index, value in enumerate(components):
            if not value.isspace():
                m = re.match("\[(.*?)\]", value)

                # we are parsing top down so insert at the start of list
                stacks[index].insert(0, m[1])

    stacks = Stacks(stacks)
    # process the instrcutions
    for line in infile:
        print(line)
        instructions = [int(x) for x in re.findall(r'\d+', line.strip())]
        stacks.move_boxes_part2(*instructions)

    print(stacks.get_stack_tops())
