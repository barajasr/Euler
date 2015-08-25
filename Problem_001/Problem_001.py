#! /usr/bin/env python
# -*- coding: iso-8859-15 -*-

# Problem 1: Multiples of 3 and 5
#--------------------------------------------------------------------
#   If we list all the natural numbers below 10 that multiples of 3
#   or 5, we get 3, 5, 6 and 9. The sum of thes is 23.
#
#   Find the sum of all the multiples of 3 or 5 below 1000.
#--------------------------------------------------------------------

def byCounting(num1, num2, endRange):
    summation = 0
    for i in xrange(num1, endRange, num1):
        summation += i
    for i in xrange(num2, endRange, num2):
        if i % num1 == 0: continue
        summation += i
    return summation

def bySet(num1, num2, endRange):
    num1Multiples =  set(range(num1, endRange, num1))
    num2Multiples = set(range(num2, endRange, num2))
    union = num1Multiples | num2Multiples
    summation = 0
    for i in union:
        summation += i
    return summation

if __name__ == '__main__':
    print 'Find the sum of all the multiples of 3 or 5 below 1000:'
    print byCounting(3, 5, 1000)
    # 233168

