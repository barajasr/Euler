#! usr/bin/env python
# -*- coding: iso-8859-15 -*-

# Problem 36: Double-base palindromes
#--------------------------------------------------------------------
# The decimal number, 585 = 10010010012 (binary), is palindromic in
# both bases.
#
# Find the sum of all numbers, less than one million, which are
# palindromic in base 10 and base 2.
#
# (Please note that the palindromic number, in either base, may not
# include leading zeros.)
#--------------------------------------------------------------------

import Problem_004 as p

# 0m0.655s
def sumOfDoubleBasePalindromes(limit):
    palindromes = []
    for i in xrange(limit+1):
        if p.isPalindrome(str(i)):
            if p.isPalindrome(toBase2(i)):
                palindromes.append(i)
    return sum(palindromes)

def toBase2(n):
    '''Converts n into binary for ∀n, n ≥ 0
       Returns nonpadded string
    '''
    if n == 0:
        return str(0)
    elif n < 0:
        return None
    binary, mod = '', 0
    while n:
        n, mod = divmod(n, 2)
        binary += str(mod)
    return binary[::-1]
        
        
def main():
    print 'Sum of Palindromes in base₁₀,₂ under 1,000,000?'
    print sumOfDoubleBasePalindromes(1000000)
    # 872187

if __name__ == '__main__':
    main()

