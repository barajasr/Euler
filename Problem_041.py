#! usr/bin/env python
# -*- coding: iso-8859-15 -*-

# Problem 41: Pandigital prime
#--------------------------------------------------------------------
# We shall say that an n-digit number is pandigital if it makes use
# of all the digits 1 to n exactly once. For example, 2143 is a 4
# digit pandigital and is also prime.
#
# What is the largest n-digit pandigital prime that exists?
#--------------------------------------------------------------------

import Problem_012 as p

def isPandigital(number):
    number = str(number)
    pandigital = [str(i) for i in xrange(1, len(number)+1)]
    return ''.join(sorted(number)) == ''.join(pandigital)

# LONNNNGGGGG and kills RAM
def largetPandigitalPrime():
    p.genPrimesESieve(987654321, True)
    index = len(p.primes)
    while index >= 1:
        prime = p.primes[index]
        if isPandigital(prime):
            return prime
        index -= 1 
    return None

# via Mathblog
# number is divisible by 3, ie not prime iff
# sum of the digits is divisble by 3
#    1+2+3+4+5+6+7+8+9 = 45
#    1+2+3+4+5+6+7+8 = 36
#    1+2+3+4+5+6+7 = 28     upper bound
#    1+2+3+4+5+6 = 21
#    1+2+3+4+5 = 15
#    1+2+3+4 = 10           possibly in this range as well
#    1+2+3 = 6
#    1+2 = 3
# 0m5.009s, huge improvement; genPrime is ≅ 0m4.934s
def largestPandigitalPrime():
    p.genPrimesESieve(7654321, True)
    index = len(p.primes)
    while index >= 1:
        prime = p.primes[index]
        if isPandigital(prime):
            return prime
        index -= 1 
    return None
    
def main():
    print 'What is the largest n-digit pandigital prime?'
    print largestPandigitalPrime()
    # 7652413

if __name__ == '__main__':
    main()

