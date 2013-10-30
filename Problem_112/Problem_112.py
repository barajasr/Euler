#! usr/bin/env python
# -*- coding: iso-8859-15 -*-

# Problem 112: Bouncy numbers
#--------------------------------------------------------------------
# Working from left-to-right if no digit is exceeded by the digit to
# its left it is called an increasing number; for example, 134468.
#
# Similarly if no digit is exceeded by the digit to its right it is
# called a decreasing number; for example, 66420.
#
# We shall call a positive integer that is neither increasing nor
# decreasing a "bouncy" number; for example, 155349.
#
# Clearly there cannot be any bouncy numbers below one-hundred, but
# just over half of the numbers below one-thousand (525) are bouncy.
# In fact, the least number for which the proportion of bouncy numbers
# first reaches 50% is 538.
#
# Surprisingly, bouncy numbers become more and more common and by the
# time we reach 21780 the proportion of bouncy numbers is equal to 90%.
#
# Find the least number for which the proportion of bouncy numbers is
# exactly 99%.
#--------------------------------------------------------------------

def isBouncyNumber(n):
    increasing = False
    decreasing = False
    string = str(n)
    for i in xrange(1, len(string)):
        if string[i-1] < string[i]:
            increasing = True
        elif string[i-1] > string[i]:
            decreasing = True

    return increasing and decreasing

def main():
    n = 99
    bouncies = 0
    while bouncies*100 < n*99:
        n += 1
        if isBouncyNumber(n):
            bouncies += 1
        
    return n

if __name__ == '__main__':
    print 'Find the least number for which the proportion of bouncy ' +\
          'numbers is exactly 99%.'
    print main()
    # 1587000

