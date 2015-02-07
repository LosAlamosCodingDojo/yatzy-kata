"""
Tests for yatzy. Meant to be run with py.test.

usage: py.test -v test_yatzy.py

"""

import yatzy
from yatzy import Category

def test_chance1():
    roll = [1, 1, 3, 3, 6]
    expected_score = 14

    score = yatzy.getScore(roll, Category.CHANCE)
    assert score == expected_score

def test_chance2():
    roll = [4, 5, 5, 6, 1]
    expected_score = 21

    score = yatzy.getScore(roll, Category.CHANCE)
    assert score == expected_score

def test_yatzy1():
    roll = [1, 1, 1, 1, 1]
    expected_score = 50

    score = yatzy.getScore(roll, Category.YATZY)
    assert score == expected_score

def test_yatzy2():
    roll = [1, 1, 1, 2, 1]
    expected_score = 0

    score = yatzy.getScore(roll, Category.YATZY)
    assert score == expected_score

def test_ones1():
    roll = [3, 3, 3, 4, 5]
    expected_score = 0

    score = yatzy.getScore(roll, Category.ONES)
    assert score == expected_score

def test_twos1():
    roll = [3, 3, 3, 4, 5]
    expected_score = 0

    score = yatzy.getScore(roll, Category.TWOS)
    assert score == expected_score

def test_threes1():
    roll = [1, 1, 2, 4, 4]
    expected_score = 0

    score = yatzy.getScore(roll, Category.THREES)
    assert score == expected_score

def test_fours1():
    roll = [1, 1, 2, 4, 4]
    expected_score = 8

    score = yatzy.getScore(roll, Category.FOURS)
    assert score == expected_score

def test_fives1():
    roll = [5, 1, 2, 5, 4]
    expected_score = 10

    score = yatzy.getScore(roll, Category.FIVES)
    assert score == expected_score

def test_sixes1():
    roll = [1, 1, 2, 4, 4]
    expected_score = 0

    score = yatzy.getScore(roll, Category.SIXES)
    assert score == expected_score

def test_pair1():
    roll = [3, 3, 3, 4, 4]
    expected_score = 8

    score = yatzy.getScore(roll, Category.PAIR)
    assert score == expected_score

def test_pair2():
    roll = [1, 1, 6, 2, 6]
    expected_score = 12

    score = yatzy.getScore(roll, Category.PAIR)
    assert score == expected_score

def test_pair3():
    roll = [3, 3, 3, 4, 1]
    expected_score = 6

    score = yatzy.getScore(roll, Category.PAIR)
    assert score == expected_score

def test_pair4():
    roll = [3, 3, 3, 3, 1]
    expected_score = 6

    score = yatzy.getScore(roll, Category.PAIR)
    assert score == expected_score

def test_pair5():
    roll = [1, 1, 3, 4, 5]
    expected_score = 2

    score = yatzy.getScore(roll, Category.PAIR)
    assert score == expected_score

def test_pair6():
    roll = [6, 3, 3, 4, 6]
    expected_score = 12

    score = yatzy.getScore(roll, Category.PAIR)
    assert score == expected_score

def test_pair7():
    roll = [3, 5, 3, 5, 1]
    expected_score = 10

    score = yatzy.getScore(roll, Category.PAIR)
    assert score == expected_score

def test_two_pair1():
    roll = [1, 1, 2, 3, 3]
    expected_score = 8

    score = yatzy.getScore(roll, Category.TWOPAIRS)
    assert score == expected_score

def test_two_pair2():
    roll = [1, 1, 2, 3, 4]
    expected_score = 0

    score = yatzy.getScore(roll, Category.TWOPAIRS)
    assert score == expected_score

def test_two_pair3():
    roll = [1, 1, 2, 2, 2]
    expected_score = 6

    score = yatzy.getScore(roll, Category.TWOPAIRS)
    assert score == expected_score

def test_two_pair4():
    roll = [1, 3, 6, 1, 3]
    expected_score = 8

    score = yatzy.getScore(roll, Category.TWOPAIRS)
    assert score == expected_score

def test_two_pair5():
    roll = [3, 3, 3, 3, 3]
    expected_score = 0

    score = yatzy.getScore(roll, Category.TWOPAIRS)
    assert score == expected_score

def test_three_of_a_kind1():
    roll = [3, 3, 3, 4, 5]
    expected_score = 9

    score = yatzy.getScore(roll, Category.THREEOFAKIND)
    assert score == expected_score

def test_three_of_a_kind2():
    roll = [3, 3, 4, 5, 6]
    expected_score = 0

    score = yatzy.getScore(roll, Category.THREEOFAKIND)
    assert score == expected_score

def test_three_of_a_kind3():
    roll = [3, 3, 3, 3, 1]
    expected_score = 9

    score = yatzy.getScore(roll, Category.THREEOFAKIND)
    assert score == expected_score

def test_three_of_a_kind4():
    roll = [1, 1, 3, 6, 1]
    expected_score = 3

    score = yatzy.getScore(roll, Category.THREEOFAKIND)
    assert score == expected_score

def test_three_of_a_kind5():
    roll = [5, 5, 5, 5, 5]
    expected_score = 15

    score = yatzy.getScore(roll, Category.THREEOFAKIND)
    assert score == expected_score

def test_four_of_a_kind1():
    roll = [2, 2, 2, 2, 5]
    expected_score = 8

    score = yatzy.getScore(roll, Category.FOUROFAKIND)
    assert score == expected_score

def test_four_of_a_kind2():
    roll = [2, 2, 2, 5, 5]
    expected_score = 0

    score = yatzy.getScore(roll, Category.FOUROFAKIND)
    assert score == expected_score

def test_four_of_a_kind3():
    roll = [2, 2, 2, 2, 2]
    expected_score = 8

    score = yatzy.getScore(roll, Category.FOUROFAKIND)
    assert score == expected_score

def test_four_of_a_kind4():
    roll = [2, 2, 3, 2, 2]
    expected_score = 8

    score = yatzy.getScore(roll, Category.FOUROFAKIND)
    assert score == expected_score

def test_small_straight1():
    roll = [1, 2, 3, 4, 5]
    expected_score = 15

    score = yatzy.getScore(roll, Category.SMALLSTRAIGHT)
    assert score == expected_score

def test_small_straight2():
    roll = [1, 2, 6, 4, 5]
    expected_score = 0

    score = yatzy.getScore(roll, Category.SMALLSTRAIGHT)
    assert score == expected_score

def test_small_straight3():
    roll = [5, 3, 2, 1, 4]
    expected_score = 15

    score = yatzy.getScore(roll, Category.SMALLSTRAIGHT)
    assert score == expected_score

def test_large_straight1():
    roll = [2, 3, 4, 5, 6]
    expected_score = 20

    score = yatzy.getScore(roll, Category.LARGESTRAIGHT)
    assert score == expected_score

def test_large_straight2():
    roll = [3, 2, 6, 4, 6]
    expected_score = 0

    score = yatzy.getScore(roll, Category.LARGESTRAIGHT)
    assert score == expected_score

def test_large_straight3():
    roll = [5, 6, 3, 2, 4]
    expected_score = 20

    score = yatzy.getScore(roll, Category.LARGESTRAIGHT)
    assert score == expected_score

def test_full_house1():
    roll = [1, 1, 2, 2, 2]
    expected_score = 8

    score = yatzy.getScore(roll, Category.FULLHOUSE)
    assert score == expected_score

def test_full_house2():
    roll = [6, 4, 6, 4, 6]
    expected_score = 26

    score = yatzy.getScore(roll, Category.FULLHOUSE)
    assert score == expected_score

def test_full_house3():
    roll = [2, 2, 3, 3, 4]
    expected_score = 0

    score = yatzy.getScore(roll, Category.FULLHOUSE)
    assert score == expected_score

def test_full_house4():
    roll = [4, 4, 4, 4, 4]
    expected_score = 0

    score = yatzy.getScore(roll, Category.FULLHOUSE)
    assert score == expected_score

