#! /usr/bin/env python
# -*- coding: iso-8859-15 -*-

# Problem 52: Permuted multiples
#--------------------------------------------------------------------
# It can be seen that the number, 125874, and its double, 251748,
# contain exactly the same digits, but in a different order.
#
# Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x,
# and 6x, contain the same digits.
#--------------------------------------------------------------------

def hasMultipleProperties(n):
    numbers = sorted(str(n))
    return numbers == sorted(str(2*n)) and numbers == sorted(str(3*n)) and \
           numbers == sorted(str(4*n)) and numbers == sorted(str(5*n)) and \
           numbers == sorted(str(6*n))

# 0m0.166s
def permutedMultiples():
    exp, end = 2, 666666666666666667
    n = 10
    while n < 10000000:
        n = 10**exp
        limit = n + (end%n)
        while n < limit:
            if hasMultipleProperties(n):
                return n
            n += 1
        exp += 1
    return None

def main():
    print 'Find the smallest integer x s.t. 2x, 3x, 4x, 5x, and 6x'+\
          ' contains the same digits.'
    print permutedMultiples()
    # 142857

if __name__ == '__main__':
    main()

