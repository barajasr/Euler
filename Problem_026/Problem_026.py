#! /usr/bin/env python
# -*- coding: iso-8859-15 -*-

# Problem 26: Reciprocal Cycles
#--------------------------------------------------------------------
# A unit fraction contains 1 in the numerator. The decimal
# representation of the unit fractions with denominators 2 to 10 are
# given:
#   1/2 =   0.5
#   1/3 =   0.(3)
#   1/4 =   0.25
#   1/5 =   0.2
#   1/6 =   0.1(6)
#   1/7 =   0.(142857)
#   1/8 =   0.125
#   1/9 =   0.(1)
#   1/10=   0.1
# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle.
# It can be seen that 1/7 has a 6-digit recurring cycle.
#
# Find the value of d  1000 for which 1/d contains the longest
# recurring cycle in its decimal fraction part.
#--------------------------------------------------------------------

'''
Note:
Vedic Mathematics Lesson 49: Recurring Decimals 1
'''
def isRecurring(d):
    return d%10 in (1,3,7,9)

def reciprocals(d):
    multiplier = 10 if d > 10 else 10%d
    remainder = multiplier
    result = [(remainder * d) % 10]
    while remainder > 1:
        remainder = (remainder * multiplier) % d
        result.append((remainder * d) % 10)
    return result

def longestRecipicalDenom(maxN):
    maxLength, n = (0, 0)
    for d in xrange(2, 1000):
        if isRecurring(d):
            length = len(reciprocals(d))
            if length > maxLength:
                maxLength = length
                n = d
    return n#, maxLength

# 0m0.053s
def main():
    print 'Find the denominator in 1/d producing the longest ' +\
          "recurring cycle in it's fraction part."
    print longestRecipicalDenom(1000)
    # 983

if __name__ == '__main__':
    main()

