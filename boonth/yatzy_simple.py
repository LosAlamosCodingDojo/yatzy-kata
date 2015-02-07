"""Implements the Yatzy Kata"""

import sys

def main(roll, category):
    singleNum = ["ones", "twos", "threes", "fours", "fives", "sixes"]
    if(category == "chance"):
        score = chance(roll)
    elif(category == "yatzy"):
        score = yatzy(roll)
    elif(category in singleNum):
        score = singleNumber(singleNum.index(category)+1, roll)
    elif(category == "pair"):
        score = pair(roll)
    elif(category == "two pairs"):
        score = twoPairs(roll)
    elif(category == "three of a kind"):
        score = threeOfKind(roll)
    elif(category == "four of a kind"):
        score = fourOfKind(roll)
    elif(category == "small straight"):
        score = smallStraight(roll)
    elif(category == "large straight"):
        score = largeStraight(roll)
    elif(category == "full house"):
        score = fullHouse(roll)
    else:
        print "invalid category: %s" % category

    print 'score = ', score

def testYatzy():
    """Tests all yatzy categories"""

    print "Testing...."

    assert chance([1, 1, 3, 3, 6]) == 14
    assert chance([4, 5, 5, 6, 1]) == 21
      
    assert yatzy([1, 1, 1, 1, 1]) == 50
    assert yatzy([1, 1, 1, 2, 1]) == 0
    
    assert singleNumber(4, [1, 1, 2, 4, 4]) == 8
    assert singleNumber(2, [2, 3, 2, 5, 1]) == 4
    assert singleNumber(1, [3, 3, 3, 4, 5]) == 0
    assert singleNumber(6, [1, 1, 2, 4, 4]) == 0
    assert singleNumber(3, [1, 1, 2, 4, 4]) == 0
    assert singleNumber(5, [5, 1, 2, 5, 4]) == 10

    assert pair([3, 3, 3, 4, 4]) == 8
    assert pair([1, 1, 6, 2, 6]) == 12
    assert pair([3, 3, 3, 4, 1]) == 6
    assert pair([3, 3, 3, 3, 1]) == 6
    assert pair([1, 1, 3, 4, 5]) == 2
    assert pair([6, 3, 3, 4, 6]) == 12
    assert pair([3, 5, 3, 5, 1]) == 10

    assert twoPairs([1, 1, 2, 3, 3]) == 8
    assert twoPairs([1, 1, 2, 3, 4]) == 0
    assert twoPairs([1, 1, 2, 2, 2]) == 6
    assert twoPairs([1, 3, 6, 1, 3]) == 8
    assert twoPairs([3, 3, 3, 3, 3]) == 0
    
    assert threeOfKind([3, 3, 3, 4, 5]) == 9
    assert threeOfKind([3, 3, 4, 5, 6]) == 0
    assert threeOfKind([3, 3, 3, 3, 1]) == 9
    assert threeOfKind([1, 1, 3, 6, 1]) == 3
    assert threeOfKind([5, 5, 5, 5, 5]) == 15
    
    assert fourOfKind([2, 2, 2, 2, 5]) == 8
    assert fourOfKind([2, 2, 2, 5, 5]) == 0
    assert fourOfKind([2, 2, 2, 2, 2]) == 8
    assert fourOfKind([2, 2, 3, 2, 2]) == 8

    assert smallStraight([1, 2, 3, 4, 5]) == 15
    assert smallStraight([1, 2, 6, 4, 5]) == 0
    assert smallStraight([5, 3, 2, 1, 4]) == 15

    assert largeStraight([2, 3, 4, 5, 6]) == 20
    assert largeStraight([3, 2, 6, 4, 6]) == 0
    assert largeStraight([5, 6, 3, 2, 4]) == 20

    assert fullHouse([1, 1, 2, 2, 2]) == 8
    assert fullHouse([6, 4, 6, 4, 6]) == 26
    assert fullHouse([2, 2, 3, 3, 4]) == 0
    assert fullHouse([4, 4, 4, 4, 4]) == 0

    print "Testing complete."


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

def singleNumber(match, roll):
    """This is an umbrella function to encompass the categories ones, twos,
    threes, fours, fives, and sixes. The argument match is the number that is
    being sought. The score is the sum of all the number that match.
    
    """

    score = 0
    for i in roll:
        if i == match:
            score += i

    return score

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
    score is 0. Note that pairs must be distinct numbers, (eg. [2, 2, 2, 2, 2]
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


if __name__ == '__main__':
    if(len(sys.argv) < 7):
        print "not enough input parameters!"
        print "syntax: python %s X X X X X CLASS" % sys.argv[0]
        testYatzy()
    else:
        category = sys.argv[-1].rstrip().lower()
        roll = []
        try:
            for x in sys.argv[1:6]:
                if int(x) not in range(1,7):
                    raise ''
                roll.append(int(x))
        except:
            print "need integers 1...6"
            sys.exit()
            
        main(roll, category)
        
        
        



