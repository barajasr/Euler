#! /usr/bin/env python
# -*- coding: iso-8859-15 -*-

# Problem 54: Poker hands
#--------------------------------------------------------------------
# In the card game poker, a hand consists of five cards and are
# ranked, from lowest to highest, in the following way:
#
#   0. High Card: Highest value card.
#   1. One Pair: Two cards of the same value.
#   2. Two Pairs: Two different pairs.
#   3. Three of a Kind: Three cards of the same value.
#   4. Straight: All cards are consecutive values.
#   5. Flush: All cards of the same suit.
#   6. Full House: Three of a kind and a pair.
#   7. Four of a Kind: Four cards of the same value.
#   8. Straight Flush: All cards are consecutive values of same suit.
#   9. Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
#
# The cards are valued in the order:
#   2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.
#
# If two players have the same ranked hands then the rank made up of
# the highest value wins; for example, a pair of eights beats a pair
# of fives (see example 1 below). But if two ranks tie, for example,
# both players have a pair of queens, then highest cards in each
# hand are compared (see example 4 below); if the highest cards tie
# then the next highest cards are compared, and so on.
#
# Consider the following five hands dealt to two players:
#
# Hand        Player 1        Player 2        Winner
#  1       5H 5C 6S 7S KD   2C 3S 8S 8D TD     Player 2
#           Pair of Fives   Pair of Eights
#  2       5D 8C 9S JS AC   2C 5C 7D 8S QH     Player 1
#         Highest card Ace Highest card Queen
#  3       2D 9C AS AH AC   3D 6D 7D TD QD     Player 2
#            Three Aces    Flush with Diamods
#  4       4D 6S 9H QH QC   3D 6D 7H QD QS     Player 1
#          Pair of Queens   Pair of Queens
#        Highest Card Nine  Highest card Seven
#  5       2H 2D 4C 4D 4S   3C 3D 3S 9S 9D     Player 1
#            Full House       Full House
#          With Three Fours With Three Threes
#  
# The file, poker.txt, contains one-thousand random hands dealt to
# two players. Each line of the file contains ten cards (separated
# by a single space): the first five are Player 1's cards and the
# last five are Player 2's cards. You can assume that all hands are
# valid (no invalid characters or repeated cards), each player's
# hand is in no specific order, and in each hand there is a clear
# winner.
#
# How many hands does Player 1 win?
#--------------------------------------------------------------------

weight = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9,
          'T':10, 'J':11, 'Q':12, 'K':13, 'A':14}

oneHand = [False for i in xrange(10)]
twoHand = [False for i in xrange(10)]
HIGH = 0
ONEPAIR = 1
TWOPAIR = 2
THREEKIND = 3
STRAIGHT =4
FLUSH = 5
FULLHOUSE = 6
FOURKIND = 7
STRIAGHTFLUSH = 8
ROYALFLUSH = 9

def hands(cards):
    '''First 5 cards are for playerOne, second set of 5 to playerTwo
       Return lists of each players cards sorted in (weight, Suit)
       form, where weight is an integer and Suit is char.
    '''
    playerOne, playerTwo = cards[:5], cards[5:]
    for card in xrange(5):
        playerOne[card] =  (weight[playerOne[card][0]], playerOne[card][1])
        playerTwo[card] = (weight[playerTwo[card][0]], playerTwo[card][1])
    playerOne.sort()
    playerTwo.sort()
    return playerOne, playerTwo
 
def isStraightOrFlush(cards):
    nth = 1
    straight = True
    flush = True
    while nth < 5 and (straight or flush):
        if straight:
            if cards[nth-1][0]+1 != cards[nth][0]:
                straight = False
        if flush:
            if cards[nth-1][1] != cards[nth][1]:
                flush = False
        nth += 1
    return straight, flush
    
    
def multiples(cards, player):
    '''Scans for pair, pairs, and three/four of a kind;
       stores results in applicable [one, two]Hand cell(s)
    '''
    value = {}
    card = 1
    while card < 5:
        if cards[card-1][0] ==  cards[card][0]:
            if cards[card][0] not in value:
                value[cards[card][0]] = 2
            else:
                value[cards[card][0]] += 1
        card += 1

    pair = False
    threeOfKind = False
    for i in value:
        cardValue = i
        numOfCards = value[i]
        if numOfCards == 2:
            if pair:
                # Two Pair
                if player == 1:
                    oneHand[TWOPAIR] = [cardValue, oneHand[ONEPAIR]]
                else:
                    twoHand[TWOPAIR] = [cardValue, twoHand[ONEPAIR]]
            elif threeOfKind:
                # Full house
                if player == 1:
                    oneHand[FULLHOUSE].append(cardValue)
                else:
                    twoHand[FULLHOUSE].append(cardValue)
            else:
                if player == 1:
                    oneHand[ONEPAIR] = cardValue
                else:
                    twoHand[ONEPAIR] = cardValue
                pair = True
        elif numOfCards == 3:
            if pair:
                # Full House
                if player == 1:
                    oneHand[FULLHOUSE] = [cardValue, oneHand[ONEPAIR]]
                else:
                    twoHand[FULLHOUSE] = [cardValue, twoHand[ONEPAIR]]
            else:
                if player == 1:
                    oneHand[THREEKIND] = cardValue
                else:
                    twoHand[THREEKIND] = cardValue
        elif numOfCards == 4:
            if player == 1:
                oneHand[FOURKIND] = cardValue
            else:
                twoHand[FOURKIND] = cardValue

# 0m0.048s
def playerOneWins():
    wins = 0
    contents = open('poker.txt').read().splitlines()
    for line in contents:
        one, two = hands(line.split())
        if whoWins(one, two) == 1:
             wins += 1
    return wins

def tieBreaker(index):
    ''' Returns who wins tieBreaker
            0 None
            1 Player 1
            2 Player 2
    '''
    # Technically, highest kicker should be tiebreaker in some cases
    if index == ONEPAIR:
        if oneHand[ONEPAIR] != twoHand[ONEPAIR]:
            return 1 if oneHand[ONEPAIR] > twoHand[ONEPAIR] else 2
        return 2
    elif index == TWOPAIR:
        if oneHand[TWOPAIR][0] != twoHand[TWOPAIR][0]:
            return 1 if oneHand[TWOPAIR][0] > twoHand[TWOPAIR][0] else 2
        elif oneHand[TWOPAIR][1] != twoHand[TWOPAIR][1]:
            return 1 if oneHand[TWOPAIR][1] > twoHand[TWOPAIR][1] else 2
        else:
            return 0
    elif index == THREEKIND:
        return 1 if oneHand[THREEKIND] > twoHand[THREEKIND] else 2
    elif index == FULLHOUSE:
        return 1 if oneHand[FULLHOUSE][0] > twoHand[FULLHOUSE][0] else 2
    elif index == FOURKIND:
        return 1 if oneHand[FOURKIND] > twoHand[FOURKIND] else 2
    elif index == HIGH or index == STRAIGHT or index == FLUSH or index == STRIAGHTFLUSH:
        if oneHand[0] != twoHand[0]:
            return 1 if oneHand[0] > twoHand[0] else 2
        return 0
    elif index == ROYALFLUSH:
        return 0
    
def whoWins(one, two):
    global oneHand
    global twoHand
    oneHand = [False for i in xrange(10)]
    twoHand = [False for i in xrange(10)]
    # highest card
    oneHand[0], twoHand[0] = one[-1][0], two[-1][0]
    oneHand[STRAIGHT], oneHand[FLUSH] = isStraightOrFlush(one)
    twoHand[STRAIGHT], twoHand[FLUSH] = isStraightOrFlush(two)

    if oneHand[STRAIGHT] and oneHand[FLUSH] and oneHand[HIGH] == 14:
        oneHand[ROYALFLUSH] = True
    elif oneHand[STRAIGHT] and oneHand[FLUSH]:
        oneHand[STRIAGHTFLUSH] = True

    if twoHand[STRAIGHT] and twoHand[FLUSH] and twoHand[HIGH] == 14:
        twoHand[ROYALFLUSH] = True
    elif twoHand[STRAIGHT] and twoHand[FLUSH]:
        twoHand[STRIAGHTFLUSH] = True

    multiples(one, 1)
    multiples(two, 2)

    i, j = 9, 9
    while i >= 0:
        if oneHand[i] != False:
            while j >= 0:
                if twoHand[j] != False:
                    if i != j:
                        return 1 if i > j else 2
                    else:
                        return tieBreaker(i)
                j -= 1
        i -= 1
    return None

def main():
    print 'How many hands does Player 1 win?'
    print playerOneWins()
    # 376 

if __name__ == '__main__':
    main()

