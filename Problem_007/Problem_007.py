#! /usr/bin/env python
# -*- coding: iso-8859-15 -*-

# Problem 7: 10001st prime
#--------------------------------------------------------------------
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we
# can see that the 6th prime is 13.
#
# What is the 10,001st prime number?
#--------------------------------------------------------------------

primes = [2, 3]

def isPrime(value):
    if value < 2:
        return False

    for prime in primes:
        if value%prime == 0:
            return False
        if prime**2 > value:
            break
    return True
        
# ≅ 0m0.181s
def nthPrime(nth):
    numOfPrimes = len(primes)
    if nth < numOfPrimes:
        return primes[nth-1]

    candidate = primes[-1]
    while numOfPrimes < nth:
        candidate += 2
        if isPrime(candidate):
            primes.append(candidate)
            numOfPrimes += 1

    return primes[nth-1]

# hkapur97 
# ≅ 0m0.048s
def problem7(n = 160000):
    l, c = (n - 1)/2, 1; a = [True] * l
    for i in xrange(200):
        if a[i]:
            s = i + i + 3; t = (s * s - 3)/2
            for j in xrange(t, l, s):
                a[j] = False

    for x in xrange(l):
        c += a[x]
        if c == 10001:
            return x + x + 3

if __name__ == '__main__':
    print "10,001st prime number:"
    print nthPrime(10001)

