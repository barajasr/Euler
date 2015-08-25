#! /usr/bin/env python
# -*- coding: iso-8859-15 -*-
import math

# Problem 3: Largest prime factor
#--------------------------------------------------------------------
# The prime factors of 13195 are 5, 7, 13, and 29.
#
# What is the largest prime factor of the number 600851475143?
#--------------------------------------------------------------------
 
def primeFactors(num):
    factors, d = ([], 2)
    while num > 1:
        while num%d == 0:
            factors.append(d)
            num /= d
        d += 1
        if d*d > num:
            if num > 1:
                factors.append(num)
            break
    return factors

if __name__ == '__main__':
    print 'Largest prime factor of the number 600851475143?'
    print primeFactors(600851475143)[-1]

