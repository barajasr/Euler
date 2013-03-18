#! usr/bin/env python
# -*- coding: iso-8859-15 -*-

# Problem 21: Amicable numbers
#--------------------------------------------------------------------
# Let d(n) be defined as the sum of proper divisors of n (numbers less
# than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a  b, then a and b are an amicable
# pair and each of a and b are called amicable numbers.
#
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20,
# 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of
# 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
#
# Evaluate the sum of all the amicable numbers under 10000.
#--------------------------------------------------------------------

import math

pairs = []
numAndSum = {}

# All even divisors possible in range [1...n-1]
def properDivisors(n):
    pDivisors = set([1])
    for i in xrange(2, int(math.sqrt(n))+1):
        if n%i == 0:
            pDivisors |= set((i, n/i))
    return pDivisors

def genPairs(maxN):
    for i in xrange(4, maxN):
        pDivisors = properDivisors(i)
        summation = sum(pDivisors)
        numAndSum[i] = summation
        if summation in numAndSum :
            if numAndSum[summation] == i and summation != i:
                pairs.append((summation, i))

def sumAmicable(maxN):
    return sum([pair[0] + pair[1] for pair in pairs])

# genPairs + sumAmicable ≅ 0m0.087s
def main():
    genPairs(10000)
    print 'Sum of all the amicable numbers under 10000.'
    print sumAmicable(10000)
    # 31626

if __name__ == '__main__':
    main()

