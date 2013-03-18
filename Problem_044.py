#! usr/bin/env python
# -*- coding: iso-8859-15 -*-

# Problem 44: Pentagon numbers
#--------------------------------------------------------------------
# Pentagonal numbers are generated by the formula, Pn=n(3n1)/2. The
# first ten pentagonal numbers are:
#   1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...
#
# It can be seen that P4 + P7 = 22 + 70 = 92 = P8. However, their
# difference, 70 + 22 = 48, is not pentagonal.
#
# Find the pair of pentagonal numbers, Pj and Pk, for which their
# sum and difference are pentagonal and D = |Pk - Pj| is minimised;
# what is the value of D?
#--------------------------------------------------------------------
# Absolutely no clue how to bound this

# 0m2.163s tottime, 2347877 ncalls 
def isPentagonal(number):
    inverse = ((1+ 24*number)**0.5 + 1)/6.0
    return int(inverse) == inverse

def nthPentagonal(nth):
    return nth*(3*nth - 1)/2

# 0m2.828s
def smallestDifferencePentagonal():
    i, found, result = 1, False, 0
    penatgonals = []
    while not found:
        i += 1
        curPentagonal = nthPentagonal(i)
        for j in xrange(i-1, 0, -1):
            prevPentagonal = nthPentagonal(j)
            if isPentagonal(curPentagonal-prevPentagonal) and \
               isPentagonal(curPentagonal + prevPentagonal):
                result = curPentagonal - prevPentagonal
                found = True
                break
    return result, curPentagonal, prevPentagonal

# hkapur97
# 0m0.197s
def alt():
    s = set()
    for n in xrange(500, 10000):
        x = (n * (3 * n - 1))/2; s.add(x)
        for y in s:
            if x - y in s and x - 2 * y in s:
                return x - 2 * y
def main():
    print 'Find the pair of pentagonal numbers, Pj and Pk, for' +\
          ' which their sum and difference are pentagonal and' +\
          ' D = |Pk -  Pj| is minimised; what is the value of D?'
    print smallestDifferencePentagonal()
    # 

if __name__ == '__main__':
    main()

