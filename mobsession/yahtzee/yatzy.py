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

    def pick_n_of_a_kind(self, n: int) -> int:
        return max(self.pick_n_of_a_kinds(n), default=0)

    def pick_two_pairs(self) -> list[int]:
        return self.pick_n_of_a_kinds(2)

    def pick_n_of_a_kinds(self, n: int) -> list[int]:
        result = []

        for i, frequency in enumerate(self.histogram, start=1):
            if frequency >= n:
                result.append(i)

        return result

    @property
    def histogram(self) -> [int]:
        return [self.dice.count(d) for d in range(1, 7)]

    def is_small_straight(self) -> bool:
        return sorted(self.dice) == [1, 2, 3, 4, 5]

    def is_large_straight(self) -> bool:
        return sorted(self.dice) == [2, 3, 4, 5, 6]

    def is_full_house(self) -> bool:
        return 2 in self.histogram and 3 in self.histogram

    def is_yatzy(self) -> bool:
        return 5 in self.histogram


class Yatzy:
    def __init__(self, d1: int, d2: int, d3: int, d4: int, d5: int) -> None:
        self.roll = Roll([d1, d2, d3, d4, d5])

    def chance(self) -> int:
        return self.roll.sum()

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
        pairs = self.roll.pick_two_pairs()

        return sum(pairs) * 2 if len(pairs) == 2 else 0

    def one_pair(self) -> int:
        return self.n_of_a_kind(2)

    def three_of_a_kind(self) -> int:
        return self.n_of_a_kind(3)

    def four_of_a_knd(self) -> int:
        return self.n_of_a_kind(4)

    def n_of_a_kind(self, n: int) -> int:
        return self.roll.pick_n_of_a_kind(n) * n

    def small_straight(self) -> int:
        return 15 if self.roll.is_small_straight() else 0

    def large_straight(self) -> int:
        return 20 if self.roll.is_large_straight() else 0

    def yatzy(self) -> int:
        return 50 if self.roll.is_yatzy() else 0

    def full_house(self) -> int:
        return self.roll.sum() if self.roll.is_full_house() else 0
