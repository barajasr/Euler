#! /usr/bin/env python
# -*- coding: iso-8859-15 -*-

# Problem 4: Largest palindrome product
#--------------------------------------------------------------------
#   A palindromic number reads the same both ways. The largest
#   palindrome made from the product of two 2-digit numbers is
#   9009 =  91·99.
#
#   Find the largest largest palindrome made from the product of
#   two 3-digit numbers.
#--------------------------------------------------------------------

def isPalindrome(string):
    return string == string[::-1]

def bruteMultiplication():
    solution = -1
    j = range(1000, 99, -1)
    for i in xrange(1000, 99, -1):
        for jj in j:
            product = i*jj
            if product > solution:
                if isPalindrome(str(product)):
                    solution = product
            else:
                break
        del j[0]    # Don't do redundant work
    return solution
 

if __name__ == '__main__':
    print 'Largest palindrome from product of two 3-digit numbers.'
    print bruteMultiplication()

