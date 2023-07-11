class Yatzy:
    def __init__(self, d1: int, d2: int, d3: int, d4: int, d5: int) -> None:
        self.dice = d1, d2, d3, d4, d5

    def chance(self) -> int:
        return sum(self.dice)

    def yatzy(self) -> int:
        result = 0
        for i in range(len(self.histogram)):
            if self.histogram[i] == 5:
                result = 50

        return result

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

    def one_pair(self):
        result = 0
        for at in range(6):
            if self.histogram[6 - at - 1] == 2:
                result = (6 - at) * 2
                break
        return result

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

    def four_of_a_knd(self):
        result = 0
        for i in range(6):
            if self.histogram[i] >= 4:
                result = (i + 1) * 4

        return result

    @property
    def histogram(self) -> [int]:
        result = [0] * 6
        for die in self.dice:
            result[die - 1] += 1

        return result

    def three_of_a_kind(self):
        result = 0
        for i in range(6):
            if self.histogram[i] >= 3:
                result = (i + 1) * 3

        return result

    def small_straight(self):
        result = 0

        if self.is_small_straight():
            result = 15

        return result

    def is_small_straight(self) -> bool:
        return sorted(self.dice) == [1, 2, 3, 4, 5]

    def large_straight(self):
        result = 0

        if self.is_large_straight():
            result = 20

        return result

    def is_large_straight(self) -> bool:
        return sorted(self.dice) == [2, 3, 4, 5, 6]

    def full_house(self) -> int:
        result = 0
        is_pair = False
        pair_at = 0
        is_triple = False
        triple_at = 0

        for i in range(6):
            if self.histogram[i] == 2:
                is_pair = True
                pair_at = i + 1
            if self.histogram[i] == 3:
                is_triple = True
                triple_at = i + 1

        if is_pair and is_triple:
            result = pair_at * 2 + triple_at * 3

        return result
