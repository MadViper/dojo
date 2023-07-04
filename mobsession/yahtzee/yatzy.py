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
        sum = 0
        if self.dice[0] == 1:
            sum += 1
        if self.dice[1] == 1:
            sum += 1
        if self.dice[2] == 1:
            sum += 1
        if self.dice[3] == 1:
            sum += 1
        if self.dice[4] == 1:
            sum += 1
        return sum

    def twos(self):
        sum = 0
        if self.dice[0] == 2:
            sum += 2
        if self.dice[1] == 2:
            sum += 2
        if self.dice[2] == 2:
            sum += 2
        if self.dice[3] == 2:
            sum += 2
        if self.dice[4] == 2:
            sum += 2
        return sum

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
        sum = 0
        for at in range(5):
            if self.dice[at] == 4:
                sum += 4
        return sum

    def fives(self):
        s = 0
        i = 0
        for i in range(len(self.dice)):
            if self.dice[i] == 5:
                s = s + 5
        return s

    def sixes(self):
        sum = 0
        for at in range(len(self.dice)):
            if self.dice[at] == 6:
                sum = sum + 6
        return sum

    def one_pair(self):
        result = 0
        counts = [0] * 6
        counts[self.dice[0] - 1] += 1
        counts[self.dice[1] - 1] += 1
        counts[self.dice[2] - 1] += 1
        counts[self.dice[3] - 1] += 1
        counts[self.dice[4] - 1] += 1
        at = 0
        for at in range(6):
            if counts[6 - at - 1] == 2:
                result = (6 - at) * 2
                break
        return result

    @staticmethod
    def two_pairs(d1, d2, d3, d4, d5):
        return Yatzy(d1, d2, d3, d4, d5).aaaa()

    def aaaa(self):
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

    @staticmethod
    def four_of_a_kind(_1, _2, d3, d4, d5):
        tallies = [0] * 6
        tallies[_1 - 1] += 1
        tallies[_2 - 1] += 1
        tallies[d3 - 1] += 1
        tallies[d4 - 1] += 1
        tallies[d5 - 1] += 1
        for i in range(6):
            if tallies[i] >= 4:
                return (i + 1) * 4
        return 0

    @staticmethod
    def three_of_a_kind(d1, d2, d3, d4, d5):
        t = [0] * 6
        t[d1 - 1] += 1
        t[d2 - 1] += 1
        t[d3 - 1] += 1
        t[d4 - 1] += 1
        t[d5 - 1] += 1
        for i in range(6):
            if t[i] >= 3:
                return (i + 1) * 3
        return 0

    @staticmethod
    def small_straight(d1, d2, d3, d4, d5):
        tallies = [0] * 6
        tallies[d1 - 1] += 1
        tallies[d2 - 1] += 1
        tallies[d3 - 1] += 1
        tallies[d4 - 1] += 1
        tallies[d5 - 1] += 1
        if (
            tallies[0] == 1
            and tallies[1] == 1
            and tallies[2] == 1
            and tallies[3] == 1
            and tallies[4] == 1
        ):
            return 15
        return 0

    @staticmethod
    def large_straight(d1, d2, d3, d4, d5):
        tallies = [0] * 6
        tallies[d1 - 1] += 1
        tallies[d2 - 1] += 1
        tallies[d3 - 1] += 1
        tallies[d4 - 1] += 1
        tallies[d5 - 1] += 1
        if (
            tallies[1] == 1
            and tallies[2] == 1
            and tallies[3] == 1
            and tallies[4] == 1
            and tallies[5] == 1
        ):
            return 20
        return 0

    @staticmethod
    def full_house(d1, d2, d3, d4, d5):
        tallies = []
        _2 = False
        i = 0
        _2_at = 0
        _3 = False
        _3_at = 0

        tallies = [0] * 6
        tallies[d1 - 1] += 1
        tallies[d2 - 1] += 1
        tallies[d3 - 1] += 1
        tallies[d4 - 1] += 1
        tallies[d5 - 1] += 1

        for i in range(6):
            if tallies[i] == 2:
                _2 = True
                _2_at = i + 1

        for i in range(6):
            if tallies[i] == 3:
                _3 = True
                _3_at = i + 1

        if _2 and _3:
            return _2_at * 2 + _3_at * 3
        else:
            return 0
