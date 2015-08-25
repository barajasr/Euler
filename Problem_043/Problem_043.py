#! /usr/bin/env python
# -*- coding: iso-8859-15 -*-

# Problem 43: Sub-string divisibility
#--------------------------------------------------------------------
# The number, 1406357289, is a 0 to 9 pandigital number because it
# is made up of each of the digits 0 to 9 in some order, but it also
# has a rather interesting sub-string divisibility property.

# Let d₁ be the 1st digit, d₂ be the 2nd digit, and so on. In this
# way, we note the following:
#
#   d₂d₃d₄  =406 is divisible by 2
#   d₃d₄d5  =063 is divisible by 3
#   d₄d₅d₆  =635 is divisible by 5
#   d₅d₆d₇  =357 is divisible by 7
#   d₆d₇d₈  =572 is divisible by 11
#   d₇d₈d₉  =728 is divisible by 13
#   d₈d₉d₁₀ =289 is divisible by 17
#Find the sum of all 0 to 9 pandigital numbers with this property.
#--------------------------------------------------------------------

import itertools

def hasDivisibleProperties(digits=[]):
    if digits != []:
        if int(digits[1]+digits[2]+digits[3])%2 != 0:
            return False
        if int(digits[2]+digits[3]+digits[4])%3 != 0:
            return False
        if int(digits[3]+digits[4]+digits[5])%5 != 0:
            return False
        if int(digits[4]+digits[5]+digits[6])%7 != 0:
            return False
        if int(digits[5]+digits[6]+digits[7])%11 != 0:
            return False
        if int(digits[6]+digits[7]+digits[8])%13 != 0:
            return False
        if int(digits[7]+digits[8]+digits[9])%17 != 0:
            return False
        return True
    return False

# 0m7.649s
def sumOfDivisiblePandigitals():
    summation = 0
    for numberList in itertools.permutations(['0','1','2','3','4','5','6','7','8','9']):
        value = int(numberList[0])
        if value != 0:
            if hasDivisibleProperties(numberList):
                for digit in numberList[1:]:
                    value = value*10 + int(digit)
                summation += value
    return summation

def main():
    print 'Sum of all 0-9 pandigital with divisible properties.'
    print sumOfDivisiblePandigitals()
    # 16695334890

if __name__ == '__main__':
    main()

