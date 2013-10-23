#! usr/bin/env python
# -*- coding: iso-8859-15 -*-

# Problem 9: Special Pythagorean triplet
#--------------------------------------------------------------------
# A Pythagorean triplet is a set of three natural numbers, a<b<c, for
# which,
#   a²+b²=c²
# For example, 3²+4² = 9+16 = 25 = 5²
#
# There exists exactly one Pythagorean triplet for which a+b+c=1000.
# Find the product abc.
#--------------------------------------------------------------------

import math
import numpy as np

def bruteSearchABC(keyValue):
    end = keyValue/2 + 1
    for a in xrange(1, end, 1):
        for b in xrange(a+1, end, 1):
            c = math.sqrt(a**2 + b**2)
            if c%1 == 0:
                c = int(c)
                summation = a+b+c
                if summation > keyValue:
                    break
                elif summation == keyValue:
                    return a*b*c
    return None

# barada
def triangle():
    for a in range(1, 1000):
        for b in range(a, 1000 - a):
            if a ** 2 + b ** 2 == (1000 - a - b) ** 2:
                return a * b * (1000 - a - b)

# boaz_R, triangle in polar coordinates
# a=rcos(θ), b=rsin(θ), c=r
# Holds the relation a²+b²=c², ∀(r,θ).
# Combining a+b+c=1000:
#   1000 = r(1+√2cos(θ-(π/4)))
# Lower limit, r > 1000/(1+√2)
# θ = π/4 + acos((1000/(r√2)-(1/√2))
# loop r from [r_min...n) and check integers(a,b)
def equal(a,b,err):
    return abs(a-b)<err

def prob9(n=1000):
    minr = int(n/(1+2**.5))
    for q in xrange(minr,n):
        theta = np.pi/4 + np.arccos((n/(q*2**.5)-2**(-.5)))
        if equal(round(q*np.sin(theta)),(q*np.sin(theta)),10**(-6)) and equal(round(q*np.cos(theta)),(q*np.cos(theta)) ,10**-6) and theta>0.005 and theta < np.pi/2.005:
            #print q,q*np.cos(theta),q*np.sin(theta)            
            return round(float(q)**3/2.*np.sin(2.*theta))
            break

if __name__ == '__main__':
    print 'Find the product abc that satisfies a+b+c=1000,',\
          'a²+b²=c, and a<b<c:'
    print bruteSearchABC(1000)

