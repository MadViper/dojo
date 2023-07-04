class Yatzy:
    def __init__(self, d1: int, d2: int, d3: int, d4: int, d5: int) -> None:
        self.dice = d1, d2, d3, d4, d5

    def chance(self) -> int:
        return sum(self.dice)

    def yatzy(self) -> int:
        result = 0
        counts = self.histogram()
        for i in range(len(counts)):
            if counts[i] == 5:
                result = 50

        return result

    def ones(self):
        total = 0
        if self.dice[0] == 1:
            total += 1
        if self.dice[1] == 1:
            total += 1
        if self.dice[2] == 1:
            total += 1
        if self.dice[3] == 1:
            total += 1
        if self.dice[4] == 1:
            total += 1
        return total

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
        counts = self.histogram()
        for at in range(6):
            if counts[6 - at - 1] == 2:
                result = (6 - at) * 2
                break
        return result

    def two_pairs(self):
        counts = self.histogram()
        n = 0
        score = 0
        for i in range(6):
            if counts[6 - i - 1] >= 2:
                n = n + 1
                score += 6 - i
        if n == 2:
            result = score * 2
        else:
            result = 0
        return result

    def four_of_a_knd(self):
        result = 0
        counts = self.histogram()
        for i in range(6):
            if counts[i] >= 4:
                result = (i + 1) * 4

        return result

    def histogram(self) -> [int]:
        result = [0] * 6
        for die in self.dice:
            result[die - 1] += 1

        return result

    def three_of_a_kind(self):
        result = 0
        counts = self.histogram()
        for i in range(6):
            if counts[i] >= 3:
                result = (i + 1) * 3

        return result

    def small_straight(self):
        result = 0
        counts = self.histogram()
        if (
            counts[0] == 1
            and counts[1] == 1
            and counts[2] == 1
            and counts[3] == 1
            and counts[4] == 1
        ):
            result = 15

        return result

    def large_straight(self):
        result = 0
        counts = self.histogram()
        if (
            counts[1] == 1
            and counts[2] == 1
            and counts[3] == 1
            and counts[4] == 1
            and counts[5] == 1
        ):
            result = 20
        return result

    def full_house(self):
        d_ = self.dice[0]
        d_1 = self.dice[1]
        d_2 = self.dice[2]
        d_3 = self.dice[3]
        d_4 = self.dice[4]
        result = 0
        _2 = False
        _2_at = 0
        _3 = False
        _3_at = 0
        tallies = [0] * 6
        tallies[d_ - 1] += 1
        tallies[d_1 - 1] += 1
        tallies[d_2 - 1] += 1
        tallies[d_3 - 1] += 1
        tallies[d_4 - 1] += 1
        for i in range(6):
            if tallies[i] == 2:
                _2 = True
                _2_at = i + 1
        for i in range(6):
            if tallies[i] == 3:
                _3 = True
                _3_at = i + 1
        if _2 and _3:
            result = _2_at * 2 + _3_at * 3
        return result
