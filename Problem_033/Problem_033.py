#! /usr/bin/env python
# -*- coding: iso-8859-15 -*-

# Problem 33: Digit cancelling fractions
#--------------------------------------------------------------------
# The fraction 49/98 is a curious fraction, as an inexperienced mathematician in
# attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct,
# is obtained by cancelling the 9s.
#
# We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
#
# There are exactly four non-trivial examples of this type of fraction, less than one in
# value, and containing two digits in the numerator and denominator.
#
# If the product of these four fractions is given in its lowest common terms, find the
# value of the denominator.
#--------------------------------------------------------------------

from __future__ import division
from fractions import Fraction

def cancellingFractions():
    product = 1
    for j in xrange (1, 100):
        for i in xrange (1, j):
            val = i / j
            if (val < 1.0 and i % 11 != 0):
                num, n = i // 10, i % 10
                den, m = j % 10, j // 10
                if (den > 0 and num / den == val and n == m):
                    print i, '/', j
                    product *= m
    return product

def main():
    print 'Sum of all 1 through 9 pandigital numbers.'
    print cancellingFractions()

if __name__ == '__main__':
    main()

