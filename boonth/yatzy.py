"""Implements the Yatzy Kata"""

import sys

#-------------------------------------------------------------------------
# begin: functions for yatzy categories
#-------------------------------------------------------------------------

def chance(roll):
    """Score is the sum of the dice roll"""

    return sum(roll)

def yatzy(roll):
    """If the roll is composed of all the same number, score is 50, otherwise
    it is 0.
    
    """
    
    n = roll[0]
    for i in roll[1:]:
        if i != n:
            return 0
        
    return 50

def singleNumber(number, roll):
    """This is an umbrella function to encompass the categories ones, twos,
    threes, fours, fives, and sixes. The argument 'number' is the number that
    is being sought. The score is the sum of all dice with that number.
    
    """

    score = 0
    for i in roll:
        if i == number:
            score += i

    return score

def ones(roll):
    """Score is the sum of the dice that read 1"""
    return singleNumber(1, roll)

def twos(roll):
    """Score is the sum of the dice that read 2"""
    return singleNumber(2, roll)

def threes(roll):
    """Score is the sum of the dice that read 3"""
    return singleNumber(3, roll)

def fours(roll):
    """Score is the sum of the dice that read 4"""
    return singleNumber(4, roll)

def fives(roll):
    """Score is the sum of the dice that read 5"""
    return singleNumber(5, roll)

def sixes(roll):
    """Score is the sum of the dice that read 6"""
    return singleNumber(6, roll)

def pair(roll):
    """Score is the sum of the two highest matching dice. Score is 0 if there
    is no pair.
    
    """

    roll = roll[:]
    roll.sort()

    for i in range(4,0,-1):
        if roll[i] == roll[i-1]:
            return roll[i]*2

    return 0

def twoPairs(roll):
    """If there are two pairs, the score is the sum of these dice. Otherwise
    score is 0. Note that pairs must be distinct numbers, (eg. [2, 2, 2, 2, 5]
    scores a 0).
    
    """

    def getPair(roll):
        # find a matching pair of numbers in the dice roll. return the pair,
        # and return a new roll with the pair removed
        newRoll = roll[:]
        maxIndex = len(roll)
        for i in range(0, maxIndex-1):
            for j in range(i+1, maxIndex):
                if roll[i] == roll[j]:
                    pair = (roll[i], roll[j])
                    newRoll.remove(roll[i])
                    newRoll.remove(roll[j])
                    return pair, newRoll

        # no pair was found, return None, along with original roll
        return None, roll

    # get the first pair, this will also remove the pair from roll
    pair1, roll = getPair(roll)

    if pair1 is None:
        # no pair found
        return 0

    # get the second pair
    pair2, roll = getPair(roll)

    if pair2 is None:
        # no second pair found
        return 0

    # check that the pairs aren't the same numbers
    if pair1[0] == pair2[0]:
        return 0

    return sum(pair1) + sum(pair2)

def threeOfKind(roll):
    """If there are three matching numbers, score is the sum of those numbers.
    Otherwise, score is 0.
    
    """

    roll = roll[:]
    roll.sort()

    for i in range(4,1,-1):
        if roll[i] == roll[i-1] == roll[i-2]:
            return roll[i]*3

    return 0

def fourOfKind(roll):
    """If there are four matching numbers, score is the sum of those numbers.
    Otherwise, score is 0.
    
    """

    roll = roll[:]
    roll.sort()

    for i in range(4,2,-1):
        if roll[i] == roll[i-1] == roll[i-2] == roll[i-3]:
            return roll[i]*4

    return 0

def smallStraight(roll):
    """If the roll is [1, 2, 3, 4, 5], then score is 15 (sum of dice),
    otherwise score is 0.
    
    """

    roll = roll[:]
    roll.sort()

    expected = [1, 2, 3, 4, 5]
    for i, e in zip(roll, expected):
        if i != e:
            return 0

    return 15

def largeStraight(roll):
    """If the roll is [2, 3, 4, 5, 6], then score is 20 (sum of dice),
    otherwise score is 0.
    
    """

    roll = roll[:]
    roll.sort()

    expected = [2, 3, 4, 5, 6]
    for i, e in zip(roll, expected):
        if i != e:
            return 0

    return 20

def fullHouse(roll):
    """If the dice have a two of a kind and a three of a kind, the score is the
    sum of all the dice, otherwise the score is 0.
    
    """

    roll = roll[:]
    roll.sort()

    # conditions to check for:
    #   - first two numbers form a pair
    #   - last two numbers form a pair
    #   - these two pairs are different numbers
    #   - the middle number matches one of the pairs
    if roll[0] == roll[1]:
        if roll[3] == roll[4]:
            if roll[0] != roll[3]:
                if roll[2] == roll[0] or roll[2] == roll[3]:
                    return sum(roll)

    return 0

#-------------------------------------------------------------------------
# end: functions for yatzy categories
#-------------------------------------------------------------------------



def main(roll, category):
    """Obtains the score for a given roll and category, and prints it out"""

    score = getScore(roll, category)
    print 'Roll:', roll, 'Category:', category, 'Score:', score

def bonusReq(roll):
    """Given a roll, return a sorted list of all categories that give it a
    non-zero score for the roll.
    
    """

    # results is a list of tuples, where each 
    # tuple is (<score>, <category name>)
    results = []

    # compute the score of the roll for each category, and record the results
    # if the score is greater than zero
    for category_name in all_categories.keys():
        score = getScore(roll, category_name)
        if score > 0:
            results.append((score, category_name))

    # sort by score, descending, then print out results
    results.sort(reverse=True)

    # print out results
    print 'Roll:', roll
    for score, category_name in results:
        print 'Category:', category_name, 'Score:', score

    return results

def getScore(roll, category):
    """Obtains the score for a given roll and category. If the category is not
    recognized, returns 0.
    
    """

    score = 0
    if all_categories.has_key(category):
        score = all_categories[category](roll)
    else:
        print "Error! -- invalid category: %s" % category
    return score


# this is essentially making the equivalent of 
# C enums for the different categories
class Category:
    CHANCE = 'chance'
    YATZY = 'yatzy'
    ONES = 'ones'
    TWOS = 'twos'
    THREES = 'threes'
    FOURS = 'fours'
    FIVES = 'fives'
    SIXES = 'sixes'
    PAIR = 'pair'
    TWOPAIRS = 'two pairs'
    THREEOFAKIND = 'three of a kind'
    FOUROFAKIND = 'four of a kind'
    SMALLSTRAIGHT = 'small straight'
    LARGESTRAIGHT = 'large straight'
    FULLHOUSE = 'full house'

# a dictionary of all the categories and their associated function
# the key is the category name as a string, and the value is the function
all_categories = {Category.CHANCE : chance,
                  Category.YATZY : yatzy,
                  Category.ONES : ones,
                  Category.TWOS: twos,
                  Category.THREES: threes,
                  Category.FOURS: fours,
                  Category.FIVES: fives,
                  Category.SIXES: sixes,
                  Category.PAIR: pair,
                  Category.TWOPAIRS: twoPairs,
                  Category.THREEOFAKIND: threeOfKind,
                  Category.FOUROFAKIND: fourOfKind,
                  Category.SMALLSTRAIGHT: smallStraight,
                  Category.LARGESTRAIGHT: largeStraight,
                  Category.FULLHOUSE: fullHouse}


if __name__ == '__main__':
    if(len(sys.argv) < 7):
        print 'not enough input parameters!'
        print 'syntax: python %s ' % sys.argv[0],
        print '<n1> <n2> <n3> <n4> <n5> <category>'
    else:
        try:
            category = sys.argv[6].rstrip().lower()
            if category not in all_categories.keys():
                raise ''
        except:
            print "Error! \'%s\' is not a known category!" % category
            sys.exit()

        roll = []
        try:
            for x in sys.argv[1:6]:
                if int(x) not in range(1,7):
                    raise ''
                roll.append(int(x))
        except:
            print "Error! Numbers need to be between 1 and 6!"
            sys.exit()

        main(roll, category)

        print ''
        print '----- Bonus Requirement -----'
        bonusReq(roll)
