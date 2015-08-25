#! /usr/bin/env python
# -*- coding: iso-8859-15 -*-

# Problem 40: Champernowne's constant
#--------------------------------------------------------------------
#An irrational decimal fraction is created by concatenating the 
# positive integers:
#   0.123456789101112131415161718192021...
#
# It can be seen that the 12th digit of the fractional part is 1.
#
# If dn represents the nth digit of the fractional part, find the
# value of the following expression.
#   d₁ · d₁₀ · d₁₀₀ · d₁₀₀₀ · d₁₀₀₀₀ · d₁₀₀₀₀₀ · d₁₀₀₀₀₀₀
#--------------------------------------------------------------------

import operator

# 0m0.106s
def champernowneDigits(nths=[1]):
    # Assumes no two or more nth digits are within the
    # the same step, each new addition of n, well within of
    # problem's parameters
    digits = []
    n, width, cummalativeWidth = 1, 1, 0
    findNth = nths[0]
    nths.remove(findNth)
    while True:
        cummalativeWidth += width
        if cummalativeWidth >= findNth:
            if cummalativeWidth > findNth:
                diff = cummalativeWidth-findNth
                # This I found very annoying first runs
                offset = 2 if n > 99 else 1
                digits.append(int(str(n)[diff-offset]))
            else:
                digits.append(int(str(n)[-1]))
            if nths != []:
                findNth = nths[0]
                nths.remove(findNth)
            else:
                break
        n += 1
        width = len(str(n))
    return digits

def champernowneDigitsProduct(nths=[1]):
    digits = champernowneDigits(nths)
    return reduce(operator.mul, digits, 1)

def main():
    print "Find the product of the 10⁰...10⁶ digits of champernowne's Constant."
    print champernowneDigitsProduct([1, 10, 100, 1000, 10000, 100000, 1000000])
    # 1*1*5*3*7*2*1 = 210

if __name__ == '__main__':
    main()

