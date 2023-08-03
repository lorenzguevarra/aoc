from dataclasses import dataclass
from enum import IntEnum
from typing import List


class Shape(IntEnum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

    def get_winning_shape(self) -> "Shape":
        """Returns the Shape that will win against self."""
        return WIN_LOSS_TABLE[self][0]

    def get_losing_shape(self) -> "Shape":
        """Returns the Shape that will lose against self."""
        return WIN_LOSS_TABLE[self][1]


@dataclass
class Round:
    elf: Shape
    you: Shape

    def get_score(self) -> int:
        score = int(self.you)
        if self.you == self.elf:
            score += 3
        elif self.elf == self.you.get_losing_shape():
            score += 6
        return score


INPUT_FILE = "input.txt"

SHAPE_TABLE = {
    "A": Shape.ROCK,
    "B": Shape.PAPER,
    "C": Shape.SCISSORS,
    "X": Shape.ROCK,
    "Y": Shape.PAPER,
    "Z": Shape.SCISSORS,
}


WIN_LOSS_TABLE = {
    Shape.ROCK: (Shape.PAPER, Shape.SCISSORS),
    Shape.PAPER: (Shape.SCISSORS, Shape.ROCK),
    Shape.SCISSORS: (Shape.ROCK, Shape.PAPER),
}
"""Maps a Shape to the Shapes that will win or lose (in order in tuple value) against it.
"""


def main() -> None:
    with open(INPUT_FILE) as f:
        strat1Rounds: List[Round] = []
        strat2Rounds: List[Round] = []
        for line in f:
            elf, you = line.strip().split()
            elfShape, yourShape = SHAPE_TABLE[elf], SHAPE_TABLE[you]
            strat1Rounds.append(Round(elfShape, yourShape))

            # Strat 2 shapes
            yourShape2 = SHAPE_TABLE[elf]  # Defaults to draw
            if you == "X":
                yourShape2 = elfShape.get_losing_shape()
            elif you == "Z":
                yourShape2 = elfShape.get_winning_shape()
            strat2Rounds.append(Round(elfShape, yourShape2))

        total_score1 = sum([r.get_score() for r in strat1Rounds])
        total_score2 = sum([r.get_score() for r in strat2Rounds])
        print(f"(Strategy 1)total score: {total_score1}")
        print(f"(Strategy 2)total score: {total_score2}")


if __name__ == "__main__":
    main()
