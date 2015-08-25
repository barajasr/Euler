#! /usr/bin/env python
# -*- coding: iso-8859-15 -*-

# Problem 23: Non-abundant sums
#--------------------------------------------------------------------
# A perfect number is a number for which the sum of its proper
# divisors is exactly equal to the number. For example, the sum of
# the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which
# means that 28 is a perfect number.
#
# A number n is called deficient if the sum of its proper divisors
# is less than n and it is called abundant if this sum exceeds n.
#
# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the
# smallest number that can be written as the sum of two abundant
# numbers is 24. By mathematical analysis, it can be shown that all
# integers greater than 28123 can be written as the sum of two
# abundant numbers. However, this upper limit cannot be reduced any
# further by analysis even though it is known that the greatest
# number that cannot be expressed as the sum of two abundant numbers
# is less than this limit.
#
# Find the sum of all the positive integers which cannot be written
# as the sum of two abundant numbers.
#--------------------------------------------------------------------

import sys
sys.path.append('../Problem_021/')
import Problem_021 as p

abundantNums = [12]
maxN = 28123
summable = [False]*(maxN+1)

def isAbundant(n):
    return sum(p.properDivisors(n)) > n

def sumOfRest():
    for n in xrange(13, maxN):
        if isAbundant(n):
            abundantNums.append(n)
    validateList()
    return sum([n for n in range(1, maxN+1) if not summable[n]])

def validateList():
    for i in xrange(len(abundantNums)):
        for j in xrange(i, len(abundantNums)):
            value = abundantNums[i]+abundantNums[j]
            if value <= maxN:
                summable[value] = True
            else:
                break

# 0m3.619s
def main():
    print 'Sum of all positive integers not summable by two ' +\
          'abundant numbers:'
    print sumOfRest()
    # 4179871

if __name__ == '__main__':
    main()

