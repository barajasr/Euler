#! /usr/bin/env python
# -*- coding: iso-8859-15 -*-

# Problem 31: Coin sums
#--------------------------------------------------------------------
# In England the currency is made up of pound, £, and pence, p, and
# there are eight coins in general circulation:
#   1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
#
# It is possible to make £2 in the following way:
#   1£1 + 150p + 220p + 15p + 12p + 31p
#
# How many different ways can £2 be made using any number of coins?
#--------------------------------------------------------------------

# 0m0.031s
def waysToChange(totalPence):
    ways = 0
    for twoPounds in xrange(totalPence, -1, -200):
        for pound in xrange(twoPounds, -1, -100):
            for fiftyPence in xrange(pound, -1, -50):
                for twentyPence in xrange(fiftyPence, -1, -20):
                    for tenPence in xrange(twentyPence, -1, -10):
                        for fivePence in xrange(tenPence, -1, -5):
                            for twoPence in xrange(fivePence, -1, -2):
                                    ways += 1
    return ways

def main():
    print 'Number of ways to make £2 using any # of coins'
    print waysToChange(200)
    # 73682

if __name__ == '__main__':
    main()

