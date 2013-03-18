#! usr/bin/env python
# -*- coding: iso-8859-15 -*-

# Problem 24: Lexicographic permutations
#--------------------------------------------------------------------
# A permutation is an ordered arrangement of objects. For example,
# 3124 is one possible permutation of the digits 1, 2, 3 and 4. If
# all of the permutations are listed numerically or alphabetically,
# we call it lexicographic order. The lexicographic permutations of 
# 0, 1 and 2 are:
#
#   012   021   102   120   201   210
#
# What is the millionth lexicographic permutation of the digits 0, 
# , 2, 3, 4, 5, 6, 7, 8 and 9?
#--------------------------------------------------------------------

from itertools import islice, permutations
import math

# maladat
# 0m0.036s
def alt(string, n):
    combo_to_go=n
    available_digits=list(string)
    faclist=[math.factorial(int(i)) for i in available_digits]
    number=[]
    for i in range(9,-1,-1):
        count=0
        while (combo_to_go>faclist[i]):
            count+=1
            combo_to_go-=faclist[i]
        number.append(available_digits.pop(count))

    return ''.join(number)

# 0m0.056s
def nthPermutation(string, n):
    return''.join(next(islice(permutations(string), n-1, None)))

def main():
    print 'What is the millionth lexicographic permutation of the ' +\
          'digits 0, 1 , 2, 3, 4, 5, 6, 7, 8 and 9?'
    print nthPermutation('0123456789', 1000000)
    # 2783915460

if __name__ == '__main__':
    main()

