#! usr/bin/env python
# -*- coding: iso-8859-15 -*-

# Problem 46: Goldbach's other conjecture
#--------------------------------------------------------------------
# It was proposed by Christian Goldbach that every odd composite
#number can be written as the sum of a prime and twice a square.
#   9 = 7 + 2·1²
#   15 = 7 + 2·2²
#   21 = 3 + 2·3²
#   25 = 7 + 2·3²
#   27 = 19 + 2·2²
#   33 = 31 + 2·1²
#
#It turns out that the conjecture was false.
#
# What is the smallest odd composite that cannot be written as the
# sum of a prime and twice a square?
#--------------------------------------------------------------------

import math
import Problem_012 as p

def isTwiceSquare(value):
    root = math.sqrt(value/2.0)
    return root == int(root)

# 0m0.207s
def golbachProvedWrong():
    p.genPrimesESieve(10000, True)
    for n in xrange(3, p.primes[len(p.primes)], 2):
        if n in p.primes.values():
            continue
        contradicted = True
        root = 0
        nthPrime = 1
        while n >= p.primes[nthPrime]:
            if isTwiceSquare(n-p.primes[nthPrime]): 
                contradicted = False
                break
            nthPrime +=1
        if contradicted:
            return n
    return 'Something is wrong here...'
        
def main():
    print 'What is the smallest odd composite that cannot be' +\
          ' written in the form n = prime + 2*i²'
    print golbachProvedWrong()
    # 5777

if __name__ == '__main__':
    main()

