#! usr/bin/env python
# -*- coding: iso-8859-15 -*-

# Problem 34: Digit factorial
#--------------------------------------------------------------------
# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
#
# Find the sum of all numbers which are equal to the sum of the
# factorial of their digits.
#
# Note: as 1! = 1 and 2! = 2 are not sums they are not included.
#--------------------------------------------------------------------

import math

# 0m4.412s
def sumOfDigitFactorials():
    digitFactorial = [math.factorial(i) for i in xrange(10)]
    limit = digitFactorial[9]*7
    totalSum = 0
    for n in xrange(10, limit+1):
        sumOfFactorials = 0
        num = n
        while num > 0:
            digit = num%10
            sumOfFactorials += digitFactorial[digit]
            num /= 10
        if sumOfFactorials == n:
            totalSum += n
    return totalSum

def main():
    print 'Sum of all numbers that equal the sum of the factorial' +\
          " of it's digits."
    print sumOfDigitFactorials()
    # 40730

if __name__ == '__main__':
    main()

