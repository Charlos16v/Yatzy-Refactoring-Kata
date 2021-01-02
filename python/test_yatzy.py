from yatzy import Yatzy
import pytest

# These unit tests can be run using the py.test framework
# available from http://pytest.org/

@pytest.mark.chance
def test_chance_scores_sum_of_all_dice():
        assert 15 == Yatzy.chance(2,3,4,5,1)
        assert 16 == Yatzy.chance(3,3,4,5,1)
        assert 15 == Yatzy.chance(1,2,3,4,5) # added.
        assert 30 == Yatzy.chance(6,6,6,6,6) # added.


@pytest.mark.yatzy
def test_yatzy():
        assert 50 == Yatzy.yatzy(4,4,4,4,4)
        assert 50 == Yatzy.yatzy(6,6,6,6,6)
        assert 0 == Yatzy.yatzy(6,6,6,6,3)
        assert 50 == Yatzy.yatzy(1,1,1,1,1) # added.


@pytest.mark.ones
def test_ones(): # change name "1s" to "ones"
        assert 1 == Yatzy.ones(1,2,3,4,5)
        assert 2 == Yatzy.ones(1,2,1,4,5)
        assert 0 == Yatzy.ones(6,2,2,4,5)
        assert 4 == Yatzy.ones(1,2,1,1,1)
        assert 5 == Yatzy.ones(1,1,1,1,1) # added.


@pytest.mark.twos
def test_twos(): # change name "2s" to "twos"
        assert 4 == Yatzy.twos(1,2,3,2,6)
        assert 10 == Yatzy.twos(2,2,2,2,2)
        assert 6 == Yatzy.twos(2,2,2,4,5) # added.
        assert 6 == Yatzy.twos(2,1,2,1,2) # added.


@pytest.mark.threes
def test_threes():
        assert 6 == Yatzy.threes(1,2,3,2,3)
        assert 12 == Yatzy.threes(2,3,3,3,3)
        assert 9 == Yatzy.threes(3,3,3,2,1) # added.
        assert 3 == Yatzy.threes(1,3,1,1,1) # added.


@pytest.mark.fours
def test_fours():
        assert 12 == Yatzy.fours(4,4,4,5,5)
        assert 8 == Yatzy.fours(4,4,5,5,5)
        assert 4 == Yatzy.fours(4,5,5,5,5) # added.
        assert 16 == Yatzy.fours(4,4,4,4,1) # added.


@pytest.mark.fives
def test_fives():
        assert 10 == Yatzy.fives(4,4,4,5,5)
        assert 15 == Yatzy.fives(4,4,5,5,5)
        assert 20 == Yatzy.fives(4,5,5,5,5) # added.
        assert 5 == Yatzy.fives(5,1,1,1,1)


@pytest.mark.sixes
def test_sixes_test():
        assert 0 == Yatzy.sixes(4,4,4,5,5)
        assert 6 == Yatzy.sixes(4,4,6,5,5)
        assert 18 == Yatzy.sixes(6,5,6,6,5) # added.
        assert 12 == Yatzy.sixes(1,1,1,6,6) # added.


@pytest.mark.one_pair
def test_one_pair():
        assert 6 == Yatzy.one_pair(3,4,3,5,6)
        assert 10 == Yatzy.one_pair(5,3,3,3,5)
        assert 12 == Yatzy.one_pair(5,3,6,6,5)
        assert 8 == Yatzy.one_pair(1,1,1,4,4) # added.
        assert 4 == Yatzy.one_pair(2,4,2,4,4) # added.


@pytest.mark.two_pair
def test_two_pair():
        assert 16 == Yatzy.two_pair(3,3,5,4,5)
        assert 18 == Yatzy.two_pair(3,3,6,6,6)
        assert 0 == Yatzy.two_pair(3,3,6,5,4)
        assert 6 == Yatzy.two_pair(1,1,1,2,2) # added.
        assert 6 == Yatzy.two_pair(1,1,2,2,3) # added.


@pytest.mark.three_of_a_kind
def test_three_of_a_kind():
        assert 9 == Yatzy.three_of_a_kind(3,3,3,4,5)
        assert 15 == Yatzy.three_of_a_kind(5,3,5,4,5)
        assert 9 == Yatzy.three_of_a_kind(3,3,3,3,5)
        assert 3 == Yatzy.three_of_a_kind(1,2,1,2,1) # added.


@pytest.mark.four_of_a_kind
def test_four_of_a_kind():
        assert 12 == Yatzy.four_of_a_kind(3,3,3,3,5)
        assert 20 == Yatzy.four_of_a_kind(5,5,5,4,5)
        assert 12 == Yatzy.four_of_a_kind(3,3,3,3,3)
        assert 0  == Yatzy.four_of_a_kind(3,3,3,2,1)
        assert 4 == Yatzy.four_of_a_kind(1,1,1,1,2)


@pytest.mark.small_straight
def test_small_straight():
        assert 15 == Yatzy.small_straight(1,2,3,4,5)
        assert 15 == Yatzy.small_straight(2,3,4,5,1)
        assert 0 == Yatzy.small_straight(1,2,2,4,5)
        assert 0 == Yatzy.small_straight(2,3,4,5,6) # added.


@pytest.mark.large_straight
def test_large_straight():
        assert 20 == Yatzy.large_straight(6,2,3,4,5)
        assert 20 == Yatzy.large_straight(2,3,4,5,6)
        assert 0 == Yatzy.large_straight(1,2,2,4,5)
        assert 0 == Yatzy.large_straight(1,2,3,4,5) # added.


@pytest.mark.full_house
def test_full_house():
        assert 18 == Yatzy.full_house(6,2,2,2,6)
        assert 18 == Yatzy.full_house(6,6,2,2,2)
        assert 0 == Yatzy.full_house(2,3,4,5,6)
        assert 16 == Yatzy.full_house(2,4,2,4,4)

