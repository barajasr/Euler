#! /usr/bin/env python
# -*- coding: iso-8859-15 -*-

# Problem 28: Number spiral diagonals
#--------------------------------------------------------------------
# Starting with the number 1 and moving to the right in a clockwise
# direction a 5 by 5 spiral is formed as follows:
#
#    74 75 76 77 78 79 80 81 82
#    73 43 44 45 46 47 48 49 50    0: 1           offset from previous
#    72 42 21 22 23 24 25 26 51    1: 3+5+7+9     2
#    71 41 20  7  8  9 10 27 52    2: 13+17+21+25 4
#    70 40 19  6  1  2 11 28 53    3: 31+37+43+49 6
#    69 39 18  5  4  3 12 29 54    4: 57+65+73+81 8
#    68 38 17 16 15 14 13 30 55    5: 91          10
#    66 37 36 35 34 33 32 31 56
#    65 64 63 62 61 60 59 58 57
# It can be verified that the sum of the numbers on the diagonals is
# 101.
#
# What is the sum of the numbers on the diagonals in a 1001 by 1001
# spiral formed in the same way?
#--------------------------------------------------------------------

# SE corner  01  03  13  31  57
#    offset    02  10  18  26
#    change      08  08  08
def sumOfDiagonals(size):
    if size%2 == 0: return None
    total = 1
    corner, change, offset = (3, 8, 2)
    for layer in xrange(1, (size/2)+1):
        number = corner
        for i in xrange(4):
            total += number
            number += 2*layer
        offset += change
        corner += offset
    return total

# 0m0.030s 
def main():
    print 'Sum of the diagonals in a 10001 x 10001 spiral matrix.'
    print sumOfDiagonals(1001)
    # 669171001

if __name__ == '__main__':
    main()

