# TODO:
# Split responsibilities
#   - Category detection
#   - Score calculator
from dataclasses import dataclass


@dataclass
class Roll:
    dice: list[int]

    def count(self, value: int) -> int:
        return self.dice.count(value)

    def sum(self) -> int:
        return sum(self.dice)

    @property
    def histogram(self) -> [int]:
        return [self.dice.count(d) for d in range(1, 7)]

    def is_small_straight(self) -> bool:
        return sorted(self.dice) == [1, 2, 3, 4, 5]

    def is_large_straight(self) -> bool:
        return sorted(self.dice) == [2, 3, 4, 5, 6]

    def is_full_house(self) -> bool:
        return 2 in self.histogram and 3 in self.histogram


class Yatzy:
    def __init__(self, d1: int, d2: int, d3: int, d4: int, d5: int) -> None:
        self.roll = Roll([d1, d2, d3, d4, d5])

    def chance(self) -> int:
        return self.roll.sum()

    def yatzy(self) -> int:
        return 50 if 5 in self.roll.histogram else 0

    def ones(self) -> int:
        return self.roll.count(1)

    def twos(self) -> int:
        return self.roll.count(2) * 2

    def threes(self) -> int:
        return self.roll.count(3) * 3

    def fours(self) -> int:
        return self.roll.count(4) * 4

    def fives(self) -> int:
        return self.roll.count(5) * 5

    def sixes(self) -> int:
        return self.roll.count(6) * 6

    def two_pairs(self) -> int:
        n = 0
        score = 0

        for i, frequency in enumerate(self.roll.histogram, start=1):
            if frequency >= 2:
                n += 1
                score += i * 2

        return score if n == 2 else 0

    def one_pair(self) -> int:
        return self.n_of_a_kind(2)

    def three_of_a_kind(self) -> int:
        return self.n_of_a_kind(3)

    def four_of_a_knd(self) -> int:
        return self.n_of_a_kind(4)

    def n_of_a_kind(self, n: int) -> int:
        result = 0
        for i, frequency in enumerate(self.roll.histogram, start=1):
            if frequency >= n:
                result = i * n
        return result

    def small_straight(self) -> int:
        return 15 if self.roll.is_small_straight() else 0

    def large_straight(self) -> int:
        return 20 if self.roll.is_large_straight() else 0

    def full_house(self) -> int:
        return self.roll.sum() if self.roll.is_full_house() else 0
