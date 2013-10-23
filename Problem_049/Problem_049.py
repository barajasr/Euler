#! usr/bin/env python
# -*- coding: iso-8859-15 -*-

# Problem 49: Prime permutations
#--------------------------------------------------------------------
# The arithmetic sequence, 1487, 4817, 8147, in which each of the
# terms increases by 3330, is unusual in two ways: (i) each of the
# three terms are prime, and, (ii) each of the 4-digit numbers are
# permutations of one another.

# There are no arithmetic sequences made up of three 1-, 2-, or 3
# digit primes, exhibiting this property, but there is one other 4
# digit increasing sequence.
#
# What 12-digit number do you form by concatenating the three terms
# in this sequence?
#--------------------------------------------------------------------

import Problem_012 as p

# 0m0.353s
def threePrimePermutations():
    p.genPrimesESieve(10000, True)
    i = 1
    nPrimes = len(p.primes)
    while i < nPrimes:
        prime = p.primes[i]
        if prime > 1000 and prime != 1487:
            sortedPrime = sorted(str(prime))
            j = i+1
            while j < nPrimes:
                secondPrime = p.primes[j]
                if sorted(str(secondPrime)) == sortedPrime:
                    diff = secondPrime - prime
                    testValue = secondPrime + diff
                    if sorted(str(testValue)) == sortedPrime and testValue in p.primes.values():
                        return str(prime) + str(secondPrime) + str(testValue)
                j += 1
        i += 1
    return None

def main():
    print 'What 12-digit number do you form by concatenating the three terms?'
    print threePrimePermutations()
    # 296962999629

if __name__ == '__main__':
    main()

