#! usr/bin/env python
# -*- coding: iso-8859-15 -*-

# Problem 58: Spiral primes
#--------------------------------------------------------------------
# Starting with 1 and spiralling anticlockwise in the following way,
# a square spiral with side length 7 is formed.
#   37 36 35 34 33 32 31
#   38 17 16 15 14 13 30
#   39 18  5  4  3 12 29
#   40 19  6  1  2 11 28
#   41 20  7  8  9 10 27
#   42 21 22 23 24 25 26
#   43 44 45 46 47 48 49
#
# It is interesting to note that the odd squares lie along the
# bottom right diagonal, but what is more interesting is that 8 out
# of the 13 numbers lying along both diagonals are prime; that is, a
# ratio of 8/13  62%.
#
# If one complete new layer is wrapped around the spiral above, a
# square spiral with side length 9 will be formed. If this process
# is continued, what is the side length of the square spiral for
# which the ratio of primes along both diagonals first falls below
# 10%?
#--------------------------------------------------------------------

# SE corner  01  03  13  31  57
#    offset    02  10  18  26
#    change      08  08  08
# 0m6.758s
def diagonalPrimesRatio(percentage=.1):
    diagonalPrimes, ratio = 0, 100.0
    layer, diagonalNumbers = 0, 1
    corner, change, offset = (3, 8, 2)
    while ratio > percentage:
        layer += 1
        number = corner
        for i in xrange(4):
            diagonalNumbers += 1
            if isPrime(number):
                diagonalPrimes += 1
            number += 2*layer
        ratio = float(diagonalPrimes)/diagonalNumbers
        offset += change
        corner += offset
    return 2*layer + 1

def isPrime(number):
    if number <= 1: return False
    if number == 2: return True
    if number%2 == 0: return True
    if number < 9: return True
    if number%3 == 0: return False
    count = 5
    while count*count <= number:
        if number%count == 0: return False
        if number%(count+2) == 0: return False
        count += 6
    return True
# 
def main():
    print 'What is the side length of the sq. spiral for primes' +\
          ' falling on the diagonals first falls under 10%?'
    print diagonalPrimesRatio()
    # 26241

if __name__ == '__main__':
    main()

