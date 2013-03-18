#! usr/bin/env python
# -*- coding: iso-8859-15 -*-

# Problem 6: Sum square difference
#--------------------------------------------------------------------
# The sum of the squares of the first ten natural numbers is,
#   1² + 2² + ... + 10² = 385
# The square of the sum of the first ten natural numbers is,
#   (1 + 2 + ... + 10)² = 55² = 3025
# Hence the difference between the sum of the squares of the first
# ten natural numbers and the square of the sum is 3025  385 = 2640.
#
# Find the difference between the sum of the squares of the first
# one hundred natural numbers and the square of the sum.
#--------------------------------------------------------------------

def difference(numRange):
    numRange = xrange(numRange+1)
    return sum(numRange)**2 - sum([x**2 for x in numRange])

def difference2(numRange):
    # Use:
    # Σi  → n(n+1)/2
    # Σi² → (n(n+1)(2n+1))/6
    sumSquares = (numRange*(numRange+1)*(2*numRange+1))/6;
    squareSum = ((numRange*(numRange+1))/2)**2;
    return squareSum - sumSquares

if __name__ == '__main__':
    print 'Difference between sum of squares and square of the',\
          'sum from [1...100]:'
    print difference2(100)

