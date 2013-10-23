#! usr/bin/env python
# -*- coding: iso-8859-15 -*-

# Problem 32: Pandigital products
#--------------------------------------------------------------------
# We shall say that an n-digit number is pandigital if it makes use
# of all the digits 1 to n exactly once; for example, the 5-digit
# number, 15234, is 1 through 5 pandigital.

# The product 7254 is unusual, as the identity, 39  186 = 7254,
# containing multiplicand, multiplier, and product is 1 through 9
# pandigital.

# Find the sum of all products whose multiplicand/multiplier/product
# identity can be written as a 1 through 9 pandigital.

# HINT: Some products can be obtained in more than one way so be
# sure to only include it once in your sum.
#--------------------------------------------------------------------

def isPandigital(a, b, c):
    string = str(a) + str(b) + str(c)
    return ''.join(sorted(string)) == '123456789'

# long
def sumOfPandigitals():
    S = set()
    target = 9876
    for i in xrange(1, target+1):
        for j in xrange(1,target+1):
            if isPandigital(i, j, i*j):
                S.add(i*j)
    return sum(S)

def alt():
    S = set()
    for x in xrange(1, 100):
        for y in xrange(100, 10000):
            if isPandigital(x, y, x*y):
                print [x, y, x*y]
                S.add(x*y)
    return sum(S)

def main():
    print 'Sum of all 1 through 9 pandigital numbers.'
    print alt()#sumOfPandigitals()
    # 

if __name__ == '__main__':
    main()

