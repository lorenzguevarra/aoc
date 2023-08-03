# /usr/bin/env python

from dataclasses import dataclass
from typing import Dict, List

PRIORITIES = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
INPUT_FILE = "input.txt"


@dataclass
class Rucksack:
    contents: str

    def get_priority(self) -> int:
        half = int(len(self.contents) / 2)
        comp1, comp2 = self.contents[:half], self.contents[half:]
        for i, c in enumerate(comp1):
            if c in comp2:
                return PRIORITIES.index(c) + 1

        raise ValueError("Invalid rucksuck format")


@dataclass
class Group:
    rucksacks: List[Rucksack]

    def get_priority(self) -> int:
        combinedContents = [set(r.contents) for r in self.rucksacks]
        count: Dict[str, int] = {}
        for content in combinedContents:
            for c in content:
                if c not in count:
                    count[c] = 1
                else:
                    count[c] += 1
                if count[c] == 3:
                    return PRIORITIES.index(c) + 1

        raise ValueError("no common type in group")


def main() -> None:
    rucksacks: List[Rucksack] = []
    with open(INPUT_FILE) as f:
        rucksacks = [Rucksack(line.rstrip()) for line in f]

    groups = [Group(rucksacks[i : i + 3]) for i in range(0, len(rucksacks), 3)]
    totalPriority = sum([r.get_priority() for r in rucksacks])
    totalGroupPriority = sum([g.get_priority() for g in groups])

    print(f"Total         : {totalPriority}")
    print(f"Total by group: {totalGroupPriority}")


if __name__ == "__main__":
    main()
