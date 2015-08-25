#! /usr/bin/env python
# -*- coding: iso-8859-15 -*-

# Problem 53: Combinatoric selections
#--------------------------------------------------------------------
# There are I exactly ten ways of selecting three from five, 12345:
#    123, 124, 125, 134, 135, 145, 234, 235, 245, and 345
#
# In combinatorics, we use the notation, ⁵C₃ = 10.
# In general,
#    ⁿCr = n!/ (r!(n-r)!), where r ≤ n, n! = n·(n1)·...·321,
#    and 0! = 1.
# It is not until n = 23, that a value exceeds one-million:
# ²³C₁₀ = 1144066.
#
# How many, not necessarily distinct, values of  nCr, for 1 ≤ n≤ 100,
# are greater than one-million?
#--------------------------------------------------------------------

factorials = [1, 1, 2]

def factorial(n):
    if n < len(factorials):
        return factorials[n]
    factorials.append(factorials[n-1]*n)
    return factorials[n]

# 0m0.033s
def values(limit=1000000):
    result = 0
    for n in xrange(1, 101):
       for r in xrange(n+1):
            if factorial(n)/(factorial(r)*factorial(n-r)) >= limit:
                result += 1
    return result

#--------------------------------------------------------------------
# MathBlog
# Using pascal triangle
# If we find a number greater than our limit of 1.000.000, just put
# 1,000,000 in the place.
# 0m0.035s
def pascalTriangle(limit=1000000):
    nlimit, result = 100, 0
    pascalTriangle =[[0 for i in range(nlimit+1)] for j in range(nlimit+1)]
    for row in xrange(len(pascalTriangle)):
        pascalTriangle[row][0] =  1

    for n in xrange(1, nlimit+1):
        for r in xrange(1, nlimit+1):
            pascalTriangle[n][r] = pascalTriangle[n-1][r] + pascalTriangle[n - 1][r - 1]
            if pascalTriangle[n][r] > limit:
                pascalTriangle[n][r] =  limit
                result += 1
    return result

def main():
    print 'How many, not necessarily distinct, values of  nCr, for' +\
          ' 1 ≤ n≤ 100, are greater than one-million?'
    print values()
    # 4075

if __name__ == '__main__':
    main()

