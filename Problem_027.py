#! usr/bin/env python
# -*- coding: iso-8859-15 -*-

# Problem 27: Quadratic primes
#--------------------------------------------------------------------
# Euler published the remarkable quadratic formula:
#
#   n² + n + 41
#
# It turns out that the formula will produce 40 primes for the
# consecutive values n = 0 to 39. However, when
# n = 40, 40² + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and
# certainly when n = 4, 41² + 41 + 41 is clearly divisible by 41.
#
# Using computers, the incredible formula  n² - 79n + 1601 was
# discovered, which produces 80 primes for the consecutive values
# n = 0 to 79. The product of the coefficients, -79 and 1601, is
# -126479.
#
# Considering quadratics of the form:
#
#   n² + an + b, where |a| < 1000 and |b| < 1000
#
# where |n| is the modulus/absolute value of n
# e.g. |11| = 11 and |4| = 4
#
# Find the product of the coefficients, a and b, for the quadratic
# expression that produces the maximum number of primes for
# consecutive values of n, starting with n = 0.
#--------------------------------------------------------------------

import Problem_012 as p

# 1m52.390s
def coefficientProducts(a=1000, b=1000):
    aMax, bMax, nMax = (0, 0, 0);
    for a in xrange(-1000, 1001): 
        for b in xrange(-1000, 1001):
            n = 0
            while p.isPrime(abs(n*n + a*n + b)):
                n += 1
            if (n > nMax):
                aMax = a
                bMax = b
                nMax = n
    return aMax*bMax

# n=0
#   n² + an + b ⇒ b, ∴ b must be prime
# n>0
#   n² + an + b is odd ∴ an + b must be even
# 0m25.009s
def coefficientProducts2():
    aMax, bMax, nMax = (0, 0, 0)
    for a in xrange(-999, 1001, 2):
        key = 1
        while p.primes[key] <= 1000:
            for sign in (1, -1):
                n = 0;
                offset = -1 if p.primes[key]%2 == 0 else 0 # Making a even if b is even
                while p.isPrime(abs(n*n + (a+offset)*n + sign*p.primes[key])):
                    n += 1
                if (n > nMax):
                    aMax = a;
                    bMax = p.primes[key];
                    nMax = n;
            key += 1
    return aMax*bMax, nMax

def main():
    p.genPrimesESieve(87400)
    print 'Product of the coefficients for which produces the ' +\
          'longest sequence of primes.'
    print coefficientProducts2()
    # -59231

if __name__ == '__main__':
    main()

