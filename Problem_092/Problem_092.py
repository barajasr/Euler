#! usr/bin/env python
# -*- coding: iso-8859-15 -*-

# Problem 92: Square digit chains
#--------------------------------------------------------------------
# A number chain is created by continuously adding the square of the
# digits in a number to form a new number until it has been seen before.
#
# For example,
#
#   44 → 32 → 13 → 10 → 1 → 1
#   85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89
#
# Therefore any chain that arrives at 1 or 89 will become stuck in an
# endless loop. What is most amazing is that EVERY starting number will
# eventually arrive at 1 or 89.
#
# How many starting numbers below ten million will arrive at 89?
#--------------------------------------------------------------------

def main():
    cache = {1:False, 89:True}
    solution = 0
    for n in xrange(10000000, 1, -1):
        chain = []
        while n != 89 and n != 1:
            if n not in cache:
                chain += [n]
            else:
                break
            n = sum([int(i)*int(i) for i in str(n)])

        for link in chain:
            cache[link] = cache[n]
        if cache[n] == True:
            solution += 1

    return solution
        

if __name__ == '__main__':
    print 'How many starting numbers below ten million will arrive at 89?'
    print main()
    # 8581146

