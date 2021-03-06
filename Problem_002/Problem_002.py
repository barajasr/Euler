#! /usr/bin/env python
# -*- coding: iso-8859-15 -*-

# Problem 2: Even Fibonacci numbers
#--------------------------------------------------------------------
# Each new term in the Fibonacci sequence is generated by adding the
# previous two terms. By starting with 1, and 2, the first 10 terms
# will be:
#   1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#
# By considering the terms in the Fibonacci sequence whose values do
# not exceed four million, find the sum of the even-valued terms.
#--------------------------------------------------------------------

import math

def evenFibSum(maxVal):
    nthFib = {1:1, 2:2}
    summation, i = (2, 2)
    while nthFib[i] < maxVal:
        i += 1
        nthFib[i] = nthFib[i-1] + nthFib[i-2]
        if nthFib[i] % 2 == 0:
            summation += nthFib[i]

    return summation        

def usingRatios(maxVal):
    # φ is approximate ratio between nth and nth+1 fib numbers
    # φ³ is approximate ratio between even fib numbers
    phiCubed = ((1+math.sqrt(5))/2)**3  # ≅ 4.236068
    summation, curEven = (0, 2)
    while curEven < maxVal:
        summation += curEven
        curEven = int(round(curEven * phiCubed))
    return summation 

if __name__ == '__main__':
    print 'Summation of even Fib numbers under 4,000,000:'
    print usingRatios(4000000)

