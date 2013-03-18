#! usr/bin/env python
# -*- coding: iso-8859-15 -*-

# Problem 38: Pandigital multiples
#--------------------------------------------------------------------
# Take the number 192 and multiply it by each of 1, 2, and 3:
#   192  1 = 192
#   192  2 = 384
#   192  3 = 576
# By concatenating each product we get the 1 to 9 pandigital,
# 192384576. We will call 192384576 the concatenated product of 
# 192 and (1,2,3)
#
# The same can be achieved by starting with 9 and multiplying by
# 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is
# the concatenated product of 9 and (1,2,3,4,5).
#
# What is the largest 1 to 9 pandigital 9-digit number that can be
# formed as the concatenated product of an integer with 
# (1,2, ... , n) where n > 1?
#--------------------------------------------------------------------

import operator

def isPanDigital(number, n=9):
    '''Returns whether it is pandigital up to desired number
    '''
    pandigital = ''.join([str(digit) for digit in xrange(1, n+1)])
    number = ''.join([str(digit) for digit in number])
    return ''.join(sorted(number)) == pandigital, int(number)

# via mathBlog
# 0m0.030s 
def largestPandigitalProductConcatenated():
    solution = 0
    for i in xrange(9387, 9234, -1):
        pandigital, solution = isPanDigital(str(i)+str(2*i))
        if pandigital:
            break
    return solution
    
def main():
    print 'What is the largest 1 to 9 pandigital 9-digit number' +\
          ' that can be formed as the concatenated product of' +\
          ' an integer with (1,2, ... , n) where n > 1?'
    print largestPandigitalProductConcatenated()
    # 

if __name__ == '__main__':
    main()

