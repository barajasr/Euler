#! usr/bin/env python
# -*- coding: iso-8859-15 -*-

# Problem 37: Truncatable primes
#--------------------------------------------------------------------
# The number 3797 has an interesting property. Being prime itself,
# it is possible to continuously remove digits from left to right,
# and remain prime at each stage: 3797, 797, 97, and 7. Similarly we
# can work from right to left: 3797, 379, 37, and 3.
#
# Find the sum of the only eleven primes that are both truncatable
# from left to right and right to left.
#
# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
#--------------------------------------------------------------------

import Problem_012 as p

# 0m1.402s
def sumOfTruncatablePrimes(n=11):
    S = []
    p.genPrimesESieve(1000000, True)
    for nth in xrange(5, len(p.primes)+1):
        prime = p.primes[nth]
        # via wiki, 83 right-truncatable primes vs 4260 left-truncatable
        # Test left to right prime building first 
        if truncatablePrime(prime, True) and truncatablePrime(prime, False):
            S.append(prime)
            n -= 1
            if n == 0:
                break
    return sum(S)

def truncatablePrime(n, leftToRight=True):
    '''Returns if all numbers of length ≤ 1 are also prime.
       leftToRight flag determines in which direction the new number
       is built up from.
    '''
    n = str(n)
    if not leftToRight:
        n = n[::-1]
    newNumber = ''
    for i in xrange(len(n)-1):
        if leftToRight:
            newNumber += n[i]
        else:
            newNumber = n[i] + newNumber
        if not p.isPrime(int(newNumber)):
            return False
    return True
    
def main():
    print 'Sum of the 11 left and right truncatable primes?'
    print sumOfTruncatablePrimes()
    # 748317

if __name__ == '__main__':
    main()

