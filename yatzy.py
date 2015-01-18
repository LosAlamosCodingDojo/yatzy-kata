
import sys

def main(roll, yatzyClass):
    ichhabekeineahnung = ["ones", "twos", "threes", "fours", "fives", "sixes"]
    if(yatzyClass == "chance"):
        score = chance(roll)
    elif(yatzyClass == "yatzy"):
        score = yatzy(roll)
    elif(yatzyClass in ichhabekeineahnung):
            score = commons(ichhabekeineahnung.index(yatzyClass)+1, roll)
    elif(yatzyClass == "pair"):
        score = pair(roll)
    elif(yatzyClass == "two pairs"):
        score = two_pairs(roll)
    elif(yatzyClass == "three of a kind"):
        score = threeOfKind(roll)
    elif(yatzyClass == "four of a kind"):
        pass
    elif(yatzyClass == "small straight"):
        pass        
    elif(yatzyClass == "large straight"):
        pass
    elif(yatzyClass == "full house"):
        pass        
    else:
        print "invalid input"
            
    print 'score = ', score

def commons(match,roll):
    score = 0
    for x in roll:
        if x == match:
            score += x
    return score

def pair(roll):
    for x in range(4,0,-1):
        if roll[x] == roll[x-1]:
            return 2*roll[x]
    return 0

def threeOfKind(roll):
    for x in range(4,1,-1):
        if roll[x] == roll[x-1] == roll[x-2]:
            return 3*roll[x]
    return 0

def fourOfKind(roll):
    for x in range(4,2,-1):
        if roll[x] == roll[x-1] == roll[x-2] == roll[x-3]:
            return 4*roll[x]
    return 0

def chance(roll):
    score = 0
    for x in roll:
        score += x
    return score

def yatzy(roll):
    
    i = roll[0]
    
    for j in roll[1:]:
        if i != j:
            return 0
        
    return 50

def testYatzy():
    print "Testing...."
    assert chance([1, 1, 3, 3, 6]) == 14
    assert chance([4, 5, 5, 6, 1]) == 21
      
    assert yatzy([1, 1, 1, 1, 1]) == 50
    assert yatzy([1, 1, 1, 2, 1]) == 0
    
    assert commons(4, [1, 1, 2, 4, 4]) == 8
    assert commons(2, [2, 3, 2, 5, 1]) == 4
    assert commons(1, [3, 3, 3, 4, 5]) == 0

    assert pair(sorted([3, 3, 3, 4, 4])) == 8
    assert pair(sorted([1, 1, 6, 2, 6])) == 12
    assert pair(sorted([3, 3, 3, 4, 1])) == 6
    assert pair(sorted([3, 3, 3, 3, 1])) == 6
    assert pair(sorted([1, 1, 3, 4, 5])) == 2
    
    assert threeOfKind(sorted([3, 3, 3, 4, 5])) == 9
    assert threeOfKind(sorted([3, 3, 4, 5, 6])) == 0
    assert threeOfKind(sorted([3, 3, 3, 3, 1])) == 9
    
    assert fourOfKind(sorted([2, 2, 2, 2, 5])) == 8
    assert fourOfKind(sorted([2, 2, 2, 5, 5])) == 0
    assert fourOfKind(sorted([2, 2, 2, 2, 2])) == 8
    print "Testing complete."

if __name__ == '__main__':
    if(len(sys.argv) < 7):
        print "not enough input parameters!"
        print "syntax: python %s X X X X X CLASS" % sys.argv[0]
        testYatzy()
    else:
        yatzyClass = sys.argv[-1].rstrip().lower()
        roll = []
        try:
            for x in sys.argv[1:6]:
                if int(x) not in range(1,7):
                    raise ''
                roll.append(int(x))
        except:
            print "need integers 1...6"
            sys.exit()
            
        roll.sort()
        main(roll, yatzyClass)
        
        
        



