#! usr/bin/env python
# -*- coding: iso-8859-15 -*-

# Problem 35: Circular primes
#--------------------------------------------------------------------
# The number, 197, is called a circular prime because all rotations
# of the digits: 197, 971, and 719, are themselves prime.
#
# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17,
# 31, 37, 71, 73, 79, and 97.
#
# How many circular primes are there below one million?
#--------------------------------------------------------------------

import Problem_012 as p

# 0m17.479s
def numOfCircularPrimes(limit):
    p.genPrimesESieve(limit, True)
    total = 0
    for prime in p.primes.values():
        string = str(prime)
        cycles = False
        for char in string:
            if int(char)%2 == 0 or int(char) == 5:
                cycles = True
                break
        length = len(string)
        if length > 1 and cycles:
            continue
        valid = True
        for rotation in xrange(length-1):
            string = string[1:] + string[0]
            if not p.isPrime(int(string)):
                valid = False
                break
        if valid:
            total += 1
    return total

def main():
    print 'Number of circular primes below 1,000,000?'
    print numOfCircularPrimes(1000000)
    # 55

if __name__ == '__main__':
    main()

