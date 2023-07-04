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

    def twos(self):
        total = 0
        if self.dice[0] == 2:
            total += 2
        if self.dice[1] == 2:
            total += 2
        if self.dice[2] == 2:
            total += 2
        if self.dice[3] == 2:
            total += 2
        if self.dice[4] == 2:
            total += 2
        return total

    def threes(self):
        s = 0
        if self.dice[0] == 3:
            s += 3
        if self.dice[1] == 3:
            s += 3
        if self.dice[2] == 3:
            s += 3
        if self.dice[3] == 3:
            s += 3
        if self.dice[4] == 3:
            s += 3
        return s

    def fours(self):
        total = 0
        for at in range(5):
            if self.dice[at] == 4:
                total += 4
        return total

    def fives(self):
        s = 0
        for i in range(len(self.dice)):
            if self.dice[i] == 5:
                s = s + 5
        return s

    def sixes(self):
        total = 0
        for at in range(len(self.dice)):
            if self.dice[at] == 6:
                total = total + 6
        return total

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
        if (
            self.histogram[0] == 1
            and self.histogram[1] == 1
            and self.histogram[2] == 1
            and self.histogram[3] == 1
            and self.histogram[4] == 1
        ):
            result = 15

        return result

    def large_straight(self):
        result = 0
        if (
            self.histogram[1] == 1
            and self.histogram[2] == 1
            and self.histogram[3] == 1
            and self.histogram[4] == 1
            and self.histogram[5] == 1
        ):
            result = 20
        return result

    def full_house(self) -> int:
        result = 0
        is_2 = False
        _2_at = 0
        is_3 = False
        _3_at = 0

        for i in range(6):
            if self.histogram[i] == 2:
                is_2 = True
                _2_at = i + 1
        for i in range(6):
            if self.histogram[i] == 3:
                is_3 = True
                _3_at = i + 1

        if is_2 and is_3:
            result = _2_at * 2 + _3_at * 3

        return result
