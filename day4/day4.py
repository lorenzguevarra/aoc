# /usr/bin/env python

from dataclasses import dataclass

INPUT_FILE = "input.txt"


@dataclass
class Pair:
    data: str

    @staticmethod
    def _is_in_range(a: range, b: range) -> bool:
        """Returns true if all elements in range a is in range b.

        This can be inlined but is provided for readability.
        """
        return a.start >= b.start and a.stop <= b.stop

    @staticmethod
    def _is_overlapping(a: range, b: range) -> bool:
        """Returns true if range a overlaps with range b.

        This can be inlined but is provided for readability.
        """
        return a.start <= b.stop and a.stop >= b.start

    def get_ranges(self) -> tuple[range, range]:
        # Split self.data by ',' then split the elements in the resulting list by '-'.
        r1, r2 = [r.split("-") for r in self.data.split(",")]
        return (range(int(r1[0]), int(r1[1])), range(int(r2[0]), int(r2[1])))

    def is_in_range(self) -> bool:
        r1, r2 = self.get_ranges()
        return Pair._is_in_range(r1, r2) or Pair._is_in_range(r2, r1)

    def is_overlapping(self) -> bool:
        r1, r2 = self.get_ranges()
        return Pair._is_overlapping(r1, r2) or Pair._is_overlapping(r2, r1)


def main() -> None:
    pairs: list[Pair] = []
    with open(INPUT_FILE) as f:
        pairs = [Pair(line.rstrip()) for line in f]

    total_in_range = sum([1 if pair.is_in_range() else 0 for pair in pairs])
    total_overlap = sum([1 if pair.is_overlapping() else 0 for pair in pairs])
    print(f"Total in range: {total_in_range}")
    print(f"Total overlap : {total_overlap}")


if __name__ == "__main__":
    main()
