# /usr/bin/env python


from dataclasses import dataclass

INPUT_FILE = "input.txt"


@dataclass
class Crate:
    name: str


@dataclass
class Move:
    count: int
    from_stack: int
    to_stack: int


class Cargo:
    def __init__(self, data: list[str]):
        self._data = data
        self._moves = list[Move]()
        self._stacks = list[list[Crate]]()

    def _parse(self) -> None:
        parse_move = False
        for line in self._data:
            if len(line.strip()) == 0:
                # Start of move data
                parse_move = True
                continue
            if parse_move:
                moves = line.split()
                self._moves.append(Move(int(moves[1]), int(moves[3]) - 1, int(moves[5]) - 1))
                continue

            cols = ["".join(line[i : i + 4]).strip() for i in range(0, len(line), 4)]

            # Ignore stacks number line
            if all([c.isnumeric() for c in cols]):
                continue

            # Initialize the number of stacks once.
            if len(self._stacks) == 0:
                # The number of columns is the number of crate stacks, so we create that
                # number of empty stacks. This also prevents out of bounds errors when we
                # add items to each stacks below.
                for _ in range(0, len(cols)):
                    self._stacks.append([])
            for i, c in enumerate(cols):
                # An empty column means there is no item to be added to the stack yet
                # so we ignore it.
                if len(c) == 0:
                    continue
                # Do not include the brackets.
                self._stacks[i].append(Crate(c[1:2]))

    def _move(self, keep_order: bool = False) -> list[list[Crate]]:
        stacks = self._stacks.copy()
        for move in self._moves:
            # Move only the most that we can from the original stack.
            m = min(len(stacks[move.from_stack]), move.count)
            to_move = stacks[move.from_stack][:m]
            idx = 0
            if keep_order:
                idx = -1
            for _ in range(0, len(to_move)):
                stacks[move.to_stack].insert(0, to_move.pop(idx))
            # Remove the moved crates
            stacks[move.from_stack] = stacks[move.from_stack][m:]

        return stacks

    def get_top_crates(self, keep_order: bool = False) -> str:
        self._moves.clear()
        self._stacks.clear()
        self._parse()
        stacks = self._move(keep_order=keep_order)
        return "".join([s[0].name for s in stacks])


def main() -> None:
    lines: list[str] = []
    with open(INPUT_FILE) as f:
        lines = [line for line in f]
    cargo = Cargo(lines)

    print(f"Top crates            : {cargo.get_top_crates()}")
    print(f"Top crates(keep order): {cargo.get_top_crates(True)}")


if __name__ == "__main__":
    main()
