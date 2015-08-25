#! /usr/bin/env python
# -*- coding: iso-8859-15 -*-

# Problem 50: Consecutive prime sum
#--------------------------------------------------------------------
# The prime 41, can be written as the sum of six consecutive
# primes:
#    41 = 2 + 3 + 5 + 7 + 11 + 13
# This is the longest sum of consecutive primes that adds to a prime
# below one-hundred.
#
# The longest sum of consecutive primes below one-thousand that adds
# to a prime, contains 21 terms, and is equal to 953.
#
# Which prime, below one-million, can be written as the sum of the
# most consecutive primes?
#--------------------------------------------------------------------

import sys
sys.path.append('../Problem_012/')
import Problem_012 as p

# LONNNNNNNG
def sumOfConsectutivePrimes(limit=1000000):
    p.genPrimesESieve(1000000, True)
    i, j = 1, 2
    runningSum, maxPrime = p.primes[i], 0
    result, longest =  runningSum, 1

    for i in xrange(1, len(p.primes)):
        j = i+1
        count = 1
        runningSum = p.primes[i]
        if runningSum >= 40:
            break
        curLongest, curMaxPrime = 2, 0
        while runningSum+p.primes[j] < limit:
            count +=1
            runningSum += p.primes[j]
            if p.isPrime(runningSum):
                curLongest = count
                curMaxPrime = runningSum
            j += 1
        if curLongest >= longest:
            result = curMaxPrime
            longest = curLongest
            print longest, result

    return longest, result

def main():
    print 'Which prime, below one-million, can be be written as' +\
          ' the sum of the most consecutive primes?'
    print sumOfConsectutivePrimes()
    # 543, 997651

if __name__ == '__main__':
    main()

