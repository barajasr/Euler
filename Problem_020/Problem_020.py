#! usr/bin/env python
# -*- coding: iso-8859-15 -*-

# Problem 20: Factorial digit sum
#--------------------------------------------------------------------
# n! means n  (n  1)  ...  3  2  1
#
# For example, 10! = 10  9  ...  3  2  1 = 3628800,
# and the sum of the digits in the number 10! is 
#   3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
#
# Find the sum of the digits in the number 100!
#--------------------------------------------------------------------

import math
import Problem_016 as p

# 0m0.031s
def main():
    print 'Find the sum of the digits in the number 100!'
    print p.sumDigits(math.factorial(100))
    # 648

if __name__ == '__main__':
    main()

