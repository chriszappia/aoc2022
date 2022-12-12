from dataclasses import dataclass
import re

@dataclass
class Pairing:
    elf1_start: int
    elf1_end: int
    elf2_start: int
    elf2_end: int

    def has_full_overlap(self) -> bool:
        return (self.elf1_start <= self.elf2_start and self.elf1_end >= self.elf2_end) \
            or (self.elf2_start <= self.elf1_start and self.elf2_end >= self.elf1_end)

    def has_some_overlap(self) -> bool:
        return self.elf1_start <= self.elf2_start <= self.elf1_end \
               or self.elf1_start <= self.elf2_end <= self.elf1_end \
               or self.elf2_start <= self.elf1_start <= self.elf2_end \
               or self.elf2_start <= self.elf1_end <= self.elf2_end


pairings = []
with open("input") as infile:
    for line in infile:
        pairings.append(Pairing(*[int(x) for x in re.split("[,-]", line.strip())]))

print(f"Full Overlaps: {len([x for x in pairings if x.has_full_overlap()])}")
print(f"Partial Overlaps: {len([x for x in pairings if x.has_some_overlap()])}")