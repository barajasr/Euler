#! /usr/bin/env python
# -*- coding: iso-8859-15 -*-

# Problem 47: Distinct primes factors
#--------------------------------------------------------------------
# The first two consecutive numbers to have two distinct prime
# factors are:
#   14 = 2·7
#   15 = 3·5
#
# The first three consecutive numbers to have three distinct prime
# factors are:
#   644 = 2²·7·23
#   645 = 3·5·43
#  646 = 2·17·19
#
# Find the first four consecutive integers to have four distinct
# primes factors. What is the first of these numbers?
#--------------------------------------------------------------------

import sys
sys.path.append('../Problem_012/')
import Problem_012 as p

# MathBlog implementation
def nOfPrimeFactors(number):
    distinct = 0
    pfactor = False
    remainder = number
    for i in xrange(1, len(p.primes)):
        prime = p.primes[i]
        if prime*prime > number:
            return distinct+1
        pfactor = False
        while remainder%prime == 0:
            pfactor = True
            remainder /= prime
        if pfactor:
            distinct += 1
        if remainder == 1:
            return distinct
    return distinct

# big bottle neck here
def DistinctPrimes(number):
    primeFactors = []
    found = False
    for i in xrange(1, len(p.primes)):
        prime = p.primes[i]
        if prime > number or found: break
        exp = 1
        value = prime**exp
        if number%value == 0:
            while number%value == 0:
                if value == number: found = True
                exp +=1
                value *= prime
            primeFactors.append((prime, exp-1))
    return primeFactors

# 0m3.033s
def firstOfFourConsecutive():
    p.genPrimesESieve(1000000, True)
    consecutivePrimes, firstPrime = 0, 2
    n = 2*3*5*7-1
    while consecutivePrimes < 4:
        n += 1
        nPrimes = nOfPrimeFactors(n)#len(DistinctPrimes(n))
        if nPrimes == 4:
            consecutivePrimes += 1
            if consecutivePrimes == 1:
               firstPrime = n
        else:
            consecutivePrimes = 0
    return firstPrime

def main():
    print 'What is the fist number, in the first four consecutive' +\
          ' integers to have four distinct prime factors.'
    print firstOfFourConsecutive()
    # 134043

if __name__ == '__main__':
    main()

