#! /usr/bin/env python
# -*- coding: iso-8859-15 -*-

# Problem 45: Triangular, pentagonal, and hexagonal
#--------------------------------------------------------------------
# Triangle, pentagonal, and hexagonal numbers are generated by the
# following formulae:
#   Triangle        Tn=n(n+1)/2     1, 3, 6, 10, 15, ...
#   Pentagonal      Pn=n(3n-1)/2     1, 5, 12, 22, 35, ...
#   Hexagonal       Hn=n(2n-1)       1, 6, 15, 28, 45, ...
# It can be verified that T285 = P165 = H143 = 40755.
#
# Find the next triangle number that is also pentagonal and hexagonal.
#--------------------------------------------------------------------

def isPentagonal(value):
    return ((((1 + 24*value) ** 0.5) + 1)/6) % 1 == 0

def isHexagonal(value):
    return ((((1 + 8*value) ** 0.5) + 1)/4) % 1 == 0

def isTriangle(value):
    return ((((1 + 8*value)**0.5)-1)/2) % 1 == 0

# via joente
# would run faster using Hexagonal as reference and checking
# pentagonal and triangular
# 0m0.090s
def findNextAlt():
    n = 286
    while True:
        t = n*(n+1)/2
        if isPentagonal(t) and isHexagonal(t):
            return t
        n += 1

# with slight mod, run almost as fast as brute counting method
# 0m0.063s
def findNextAlt2():
    n = 286
    while True:
        h = n*(2*n-1)
        if isPentagonal(t) and isTriangle(t):
            return t
        n += 1

# brute counting
# 0m0.059s
def findNext():
    nT, Tn = 285, 40755
    nP, Pn = 165, 40755
    nH = 143
    #Hn ≥ Pn ≥ Tn
    while True:
        nH +=1
        Hn = nH*(2*nH-1)
        while Pn <= Hn:
            if Pn == Hn:
                while Tn <= Pn:
                    if Tn == Pn:
                        return Tn
                    nT += 1
                    Tn = (nT*(nT+1))/2
            nP += 1
            Pn = (nP*(3*nP-1))/2

def main():
    print 'What is the next triangle number equal to both ' +\
          'pentagonal and hexagonal beyong 40755?'
    print findNext()
    # 1533776805

if __name__ == '__main__':
    main()

