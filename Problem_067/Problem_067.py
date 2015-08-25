#! /usr/bin/env python
# -*- coding: iso-8859-15 -*-

# Problem 67: Maximum path sum II
#--------------------------------------------------------------------
# By starting at the top of the triangle below and moving to adjacent
# numbers on the row below, the maximum total from top to bottom is 23.
#
#    3
#   7 4
#  2 4 6
# 8 5 9 3
#
# That is, 3 + 7 + 4 + 9 = 23.
#
# Find the maximum total from top to bottom in triangle.txt (right
# click and 'Save Link/Target As...'), a 15K text file containing a
# triangle with one-hundred rows.
#
# NOTE: This is a much more difficult version of Problem 18. It is
# not possible to try every route to solve this problem, as there are
# 299 altogether! If you could check one trillion (1012) routes every
# second it would take over twenty billion years to check them all.
# There is an efficient algorithm to solve it. ;o)
#--------------------------------------------------------------------

def greatestPathSum():
    f = open('triangle.txt')
    data = [[int(n) for n in line.split()] for line in f.readlines()]
    size = len(data)

    # Select the greatest child node and push the values to root
    for row in xrange(size-2, -1, -1):
        for col in xrange(len(data[row])):
            data[row][col] += max(data[row+1][col], data[row+1][col+1])
    return data[0][0]

def main():
    print 'Path with greatest sum:'
    print greatestPathSum()
    # 7273

if __name__ == '__main__':
    main()

