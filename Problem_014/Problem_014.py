#! /usr/bin/env python
# -*- coding: iso-8859-15 -*-

# Problem 14: Longest Collatz sequence
#--------------------------------------------------------------------
# The following iterative sequence is defined for the set of positive
# integers:
#   n →  n/2    (n is even)
#   n → 3n + 1  (n is odd)
#
# Using the rule above and starting with 13, we generate the
# following sequence:
#   13  40  20  10  5  16  8  4  2  1
#
# It can be seen that this sequence (starting at 13 and finishing at 
# 1) contains 10 terms. Although it has not been proved yet (Collatz
# Problem), it is thought that all starting numbers finish at 1.
#
# Which starting number, under one million, produces the longest
# chain?
# NOTE: Once the chain starts the terms are allowed to go above one million.
#--------------------------------------------------------------------

chains = {1:1, 2:2}

def buildPath(n):
    path = []
    i = n
    while i not in chains:
        #path = [i] + path
        path.append(i)
        i = nextNumber(i)
   
    length = chains[i] + 1
    path.reverse()
    for offset in xrange(len(path)):
        chains[path[offset]] = length + offset
        
 
def longestCollatz(maxN):
    for n in xrange(3, maxN):
        if n in chains:
            continue
        buildPath(n)

    longest, start = (0, 1)
    for i in chains:
        length = chains[i]
        if length > longest:
            longest = length
            start = i
    return start

def nextNumber(n):
    if n%2 == 0:
        return n/2
    return 3*n +1

# 0m2.987s
def main():
    print 'Longest Collatz sequence:'
    print longestCollatz(1000000)
    # 837799

if __name__ == '__main__':
    main()
