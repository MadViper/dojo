class Yatzy:
    def __init__(self, d1: int, d2: int, d3: int, d4: int, d5: int) -> None:
        self.dice = d1, d2, d3, d4, d5

    def chance(self) -> int:
        return sum(self.dice)

    def yatzy(self) -> int:
        return 50 if 5 in self.histogram else 0

    def ones(self) -> int:
        return self.dice.count(1)

    def twos(self) -> int:
        return self.dice.count(2) * 2

    def threes(self) -> int:
        return self.dice.count(3) * 3

    def fours(self) -> int:
        return self.dice.count(4) * 4

    def fives(self) -> int:
        return self.dice.count(5) * 5

    def sixes(self) -> int:
        return self.dice.count(6) * 6

    def two_pairs(self):
        n = 0
        score = 0
        for i in range(6):
            if self.histogram[6 - i - 1] >= 2:
                n = n + 1
                score += 6 - i
        if n == 2:
            result = score * 2
        else:
            result = 0
        return result

    def one_pair(self) -> int:
        return self.n_of_a_kind(2)

    def three_of_a_kind(self) -> int:
        return self.n_of_a_kind(3)

    def four_of_a_knd(self) -> int:
        return self.n_of_a_kind(4)

    def n_of_a_kind(self, n: int) -> int:
        result = 0
        for i, frequency in enumerate(self.histogram, start=1):
            if frequency >= n:
                result = i * n
        return result

    @property
    def histogram(self) -> [int]:
        return [self.dice.count(d) for d in range(1, 7)]

    def small_straight(self):
        return 15 if self.is_small_straight() else 0

    def is_small_straight(self) -> bool:
        return sorted(self.dice) == [1, 2, 3, 4, 5]

    def large_straight(self):
        return 20 if self.is_large_straight() else 0

    def is_large_straight(self) -> bool:
        return sorted(self.dice) == [2, 3, 4, 5, 6]

    def full_house(self) -> int:
        return sum(self.dice) if self.is_full_house() else 0

    def is_full_house(self) -> bool:
        return 2 in self.histogram and 3 in self.histogram
