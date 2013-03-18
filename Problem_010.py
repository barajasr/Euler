#! usr/bin/env python
# -*- coding: iso-8859-15 -*-

# Problem 10: Summation of primes
#--------------------------------------------------------------------
# The sum of the primes below 10 is 2+3+4+5+7=17.
#
# Find the sum of all the primes below two million.
#--------------------------------------------------------------------

import Problem_007 as primes
from itertools import takewhile

# ≅ 7.1s 
def sumPrimes(maxValue):
    primes.primes = [2, 3]
    while primes.primes[-1] < maxValue:
        primes.nthPrime(len(primes.primes)+1)
    return sum(primes.primes[0:len(primes.primes)-1])

# zachDenton
# ≅ 0m2.984s
def eratosthenes():
    '''Yields the sequence of prime numbers via the Sieve of Eratosthenes.'''
    D = {}  # map composite integers to primes witnessing their compositeness
    q = 2   # first integer to test for primality
    while 1:
        if q not in D:
            yield q        # not marked composite, must be prime
            D[q*q] = [q]   # first multiple of q not already marked
        else:
            for p in D[q]: # move each witness to its next multiple
                D.setdefault(p+q,[]).append(p)
            del D[q]       # no longer need D[q], free memory
        q += 1

if __name__ == '__main__':
    print 'Sum of all the primes below 2,000,000:'
    #print sumPrimes(2000000)
    print sum(takewhile(lambda x: x < 2000000, eratosthenes()))
