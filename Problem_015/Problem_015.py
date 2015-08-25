#! /usr/bin/env python
# -*- coding: iso-8859-15 -*-

# Problem 15: Lattice paths
#--------------------------------------------------------------------
# Starting in the top left corner of a 22 grid, and only being able
# to move to the right and down, there are exactly 6 routes to the
# bottom right corner.
#
# How many such routes are there through a 20x20 grid?
#--------------------------------------------------------------------

import math

# Use of Pascal's triangle
# calc with Combinations
#   C(n,k) = n!/(k!(n-k)!)
#   C(4, 2) for 2x2
#   C(6, 3) for 3x3
#   C(2x, x) in general for x sides
# 0m0.033s
def routes(size):
    numerator = math.factorial(size*2)
    denom = math.factorial(size)**2
    return numerator/denom

def main():
    print 'Routes throug a 20x20 grid:'
    print routes(20)
    # 137846528820

if __name__ == '__main__':
    main()
