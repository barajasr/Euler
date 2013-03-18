#! usr/bin/env python
# -*- coding: iso-8859-15 -*-

# Problem 56: Powerful digit sum
#--------------------------------------------------------------------
# A googol (10¹⁰⁰) is a massive number: one followed by one-hundred
# zeros; 100¹⁰⁰ is almost unimaginably large: one followed by two
# hundred zeros. Despite their size, the sum of the digits in each
# number is only 1.

# Considering natural numbers of the form, a^b, where a, b < 100,
# what is the maximum digital sum?
#--------------------------------------------------------------------

# 0m0.467s
def maxDigitalSum(limit=100):
    result = 0
    for a in xrange(1, limit):
        for b in xrange(1, limit):
            summation = sum(int(digit) for digit in str(a**b))
            if summation > result:
                result = summation

    return result

def main():
    print 'What is the maximum digital sum, for a^b; a,b < 100?'
    print maxDigitalSum()
    # 972

if __name__ == '__main__':
    main()

