#! /usr/bin/env python
# -*- coding: iso-8859-15 -*-

# Problem 30: Digit fifth powers
#--------------------------------------------------------------------
# Surprisingly there are only three numbers that can be written as 
# the sum of fourth powers of their digits:
#
#   1634 = 1⁴ + 6⁴ + 3⁴ + 4⁴
#   8208 = 8⁴ + 2⁴ + 0⁴ + 8⁴
#   9474 = 9⁴ + 4⁴ + 7⁴ + 4⁴
# As 1 = 1⁴ is not a sum it is not included.
#
# The sum of these numbers is 1634 + 8208 + 9474 = 19316.
#
# Find the sum of all the numbers that can be written as the sum of 
# fifth powers of their digits.
#--------------------------------------------------------------------

def sumOfNthPowers(n):
    limit = (10**(n+1)) / n
    S = set()
    for i in xrange(2, limit):
        num = str(i)
        summation = 0
        for digit in num:
            summation += int(digit)**n
        if summation == i:
            S.update([i])
    return sum(S)

# 0m1.043s
def main():
    print 'How many distinct terms are in the sequence generated by ' +\
          'a**b for 2 ≤ a ≤ 100 and 2 ≤ b ≤ 100?'
    print sumOfNthPowers(5)
    # 443839

if __name__ == '__main__':
    main()

