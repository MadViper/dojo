from .yatzy import Yatzy


def test_chance_scores_sum_of_all_dice():
    assert Yatzy(2, 3, 4, 5, 1).chance(2, 3, 4, 5, 1) == 15
    assert Yatzy(3, 3, 4, 5, 1).chance(3, 3, 4, 5, 1) == 16


def test_yatzy_scores_50():
    assert Yatzy(4, 4, 4, 4, 4).yatzy(4, 4, 4, 4, 4) == 50
    assert Yatzy(6, 6, 6, 6, 6).yatzy(6, 6, 6, 6, 6) == 50
    assert Yatzy(6, 6, 6, 6, 3).yatzy(6, 6, 6, 6, 3) == 0


def test_ones():
    assert Yatzy(1, 2, 3, 4, 5).ones(1, 2, 3, 4, 5) == 1
    assert Yatzy(1, 2, 1, 4, 5).ones(1, 2, 1, 4, 5) == 2
    assert Yatzy(6, 2, 2, 4, 5).ones(6, 2, 2, 4, 5) == 0
    assert Yatzy(1, 2, 1, 1, 1).ones(1, 2, 1, 1, 1) == 4


def test_twos():
    assert Yatzy(1, 2, 3, 2, 6).twos(1, 2, 3, 2, 6) == 4
    assert Yatzy(2, 2, 2, 2, 2).twos(2, 2, 2, 2, 2) == 10


def test_threes():
    assert Yatzy(1, 2, 3, 2, 3).threes(1, 2, 3, 2, 3) == 6
    assert Yatzy(2, 3, 3, 3, 3).threes(2, 3, 3, 3, 3) == 12


def test_fours():
    assert Yatzy(4, 4, 4, 5, 5).fours() == 12
    assert Yatzy(4, 4, 5, 5, 5).fours() == 8
    assert Yatzy(4, 5, 5, 5, 5).fours() == 4


def test_fives():
    assert Yatzy(4, 4, 4, 5, 5).fives() == 10
    assert Yatzy(4, 4, 5, 5, 5).fives() == 15
    assert Yatzy(4, 5, 5, 5, 5).fives() == 20


def test_sixes():
    assert Yatzy(4, 4, 4, 5, 5).sixes() == 0
    assert Yatzy(4, 4, 6, 5, 5).sixes() == 6
    assert Yatzy(6, 5, 6, 6, 5).sixes() == 18


def test_one_pair():
    assert Yatzy(3, 4, 3, 5, 6).one_pair(3, 4, 3, 5, 6) == 6
    assert Yatzy(5, 3, 3, 3, 5).one_pair(5, 3, 3, 3, 5) == 10
    assert Yatzy(5, 3, 6, 6, 5).one_pair(5, 3, 6, 6, 5) == 12


def test_two_pairs():
    assert Yatzy(3, 3, 5, 4, 5).two_pairs(3, 3, 5, 4, 5) == 16
    assert Yatzy(3, 3, 6, 6, 6).two_pairs(3, 3, 6, 6, 6) == 18
    assert Yatzy(3, 3, 6, 5, 4).two_pairs(3, 3, 6, 5, 4) == 0


def test_three_of_a_kind():
    assert Yatzy(3, 3, 3, 4, 5).three_of_a_kind(3, 3, 3, 4, 5) == 9
    assert Yatzy(5, 3, 5, 4, 5).three_of_a_kind(5, 3, 5, 4, 5) == 15
    assert Yatzy(3, 3, 3, 3, 5).three_of_a_kind(3, 3, 3, 3, 5) == 9


def test_four_of_a_knd():
    assert Yatzy(3, 3, 3, 3, 5).four_of_a_kind(3, 3, 3, 3, 5) == 12
    assert Yatzy(5, 5, 5, 4, 5).four_of_a_kind(5, 5, 5, 4, 5) == 20
    assert Yatzy(3, 3, 3, 3, 3).four_of_a_kind(3, 3, 3, 3, 3) == 12
    assert Yatzy(3, 3, 3, 2, 1).four_of_a_kind(3, 3, 3, 2, 1) == 0


def test_small_straight():
    assert Yatzy(1, 2, 3, 4, 5).small_straight(1, 2, 3, 4, 5) == 15
    assert Yatzy(2, 3, 4, 5, 1).small_straight(2, 3, 4, 5, 1) == 15
    assert Yatzy(1, 2, 2, 4, 5).small_straight(1, 2, 2, 4, 5) == 0


def test_large_straight():
    assert Yatzy(6, 2, 3, 4, 5).large_straight(6, 2, 3, 4, 5) == 20
    assert Yatzy(2, 3, 4, 5, 6).large_straight(2, 3, 4, 5, 6) == 20
    assert Yatzy(1, 2, 2, 4, 5).large_straight(1, 2, 2, 4, 5) == 0


def test_full_house():
    assert Yatzy(6, 2, 2, 2, 6).full_house(6, 2, 2, 2, 6) == 18
    assert Yatzy(2, 3, 4, 5, 6).full_house(2, 3, 4, 5, 6) == 0
