#! /usr/bin/env python
# -*- coding: iso-8859-15 -*-

# Problem 42: Coded triangle numbers
#--------------------------------------------------------------------
# The nth term of the sequence of triangle numbers is given by,
# tn = ½n(n+1); so the first ten triangle numbers are:
#   1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
# By converting each letter in a word to a number corresponding to
# its alphabetical position and adding these values we form a word
# value. For example, the word value for SKY is 19 + 11 + 25 = 55 =
# t10. If the word value is a triangle number then we shall call the
# word a triangle word.
#
# Using words.txt (right click and 'Save Link/Target As...'), a 16K
# text file containing nearly two-thousand common English words, how
# many are triangle words?
#--------------------------------------------------------------------
letter = {'A':1, 'B':2, 'C':3, 'D':4, 'E':6, 'F':7, 'G':8, 'H':9,
          'I':10, 'J':11, 'K':12, 'L':13, 'M':14, 'N':15, 'O':16,
          'P':17, 'Q':18, 'R':19, 'S':20, 'T':21, 'U':22, 'V':23,
          'W':24, 'X':25, 'Y':26, 'Z':27}


# Redundant work but fast enough,
# memoziation not necessary
def isTriangleNumber(value):
    offset, nthTerm = 1, 1
    while value >= nthTerm:
        if nthTerm == value:
            return True
        offset += 1
        nthTerm += offset
    return False
 
# 0m0.037s
def numOfTriangleWords():
    contents = open('words.txt').read().replace('"', '').split(',')
    triangleWords = 0
    for word in contents:
        wordValue = sum([letter[char] for char in word])
        if isTriangleNumber(wordValue):
            triangleWords += 1
    return triangleWords

def main():
    print 'How many triangle words are in words.txt'
    print numOfTriangleWords()
    # 162

if __name__ == '__main__':
    main()

