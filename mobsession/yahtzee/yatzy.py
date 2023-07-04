class Yatzy:
    def __init__(self, d1, d2, d3, d4, _5):
        self.dice = [0] * 5
        self.dice[0] = d1
        self.dice[1] = d2
        self.dice[2] = d3
        self.dice[3] = d4
        self.dice[4] = _5

    def chance(self):
        total = 0
        total += self.dice[0]
        total += self.dice[1]
        total += self.dice[2]
        total += self.dice[3]
        total += self.dice[4]

        return total

    def yatzy(self):
        result = 0
        counts = [0] * (len(self.dice) + 1)
        for die in self.dice:
            counts[die - 1] += 1
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
        counts = [0] * 6
        counts[self.dice[0] - 1] += 1
        counts[self.dice[1] - 1] += 1
        counts[self.dice[2] - 1] += 1
        counts[self.dice[3] - 1] += 1
        counts[self.dice[4] - 1] += 1
        for at in range(6):
            if counts[6 - at - 1] == 2:
                result = (6 - at) * 2
                break
        return result

    def two_pairs(self):
        counts = [0] * 6
        counts[self.dice[0] - 1] += 1
        counts[self.dice[1] - 1] += 1
        counts[self.dice[2] - 1] += 1
        counts[self.dice[3] - 1] += 1
        counts[self.dice[4] - 1] += 1
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
        tallies = [0] * 6
        tallies[self.dice[0] - 1] += 1
        tallies[self.dice[1] - 1] += 1
        tallies[self.dice[2] - 1] += 1
        tallies[self.dice[3] - 1] += 1
        tallies[self.dice[4] - 1] += 1
        for i in range(6):
            if tallies[i] >= 4:
                result = (i + 1) * 4

        return result

    def three_of_a_kind(self):
        result = 0
        t = [0] * 6
        t[self.dice[0] - 1] += 1
        t[self.dice[1] - 1] += 1
        t[self.dice[2] - 1] += 1
        t[self.dice[3] - 1] += 1
        t[self.dice[4] - 1] += 1
        for i in range(6):
            if t[i] >= 3:
                result = (i + 1) * 3
        return result

    def small_straight(self):
        result = 0
        tallies = [0] * 6
        tallies[self.dice[0] - 1] += 1
        tallies[self.dice[1] - 1] += 1
        tallies[self.dice[2] - 1] += 1
        tallies[self.dice[3] - 1] += 1
        tallies[self.dice[4] - 1] += 1
        if (
            tallies[0] == 1
            and tallies[1] == 1
            and tallies[2] == 1
            and tallies[3] == 1
            and tallies[4] == 1
        ):
            result = 15
        return result

    def large_straight(self):
        result = 0
        tallies = [0] * 6
        tallies[self.dice[0] - 1] += 1
        tallies[self.dice[1] - 1] += 1
        tallies[self.dice[2] - 1] += 1
        tallies[self.dice[3] - 1] += 1
        tallies[self.dice[4] - 1] += 1
        if (
            tallies[1] == 1
            and tallies[2] == 1
            and tallies[3] == 1
            and tallies[4] == 1
            and tallies[5] == 1
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
