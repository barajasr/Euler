#! usr/bin/env python
# -*- coding: iso-8859-15 -*-

# Problem 16: Power digit sum
#--------------------------------------------------------------------
# 2¹⁵ = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#
# What is the sum of the digits of the 2¹⁰⁰⁰?
#--------------------------------------------------------------------

# 0m0.028s
def sumDigits(value):
    return  sum(int(x) for x in str(value))

def main():
    print 'What is the sum of the digits of the 2¹⁰⁰⁰?'
    print sumDigits(2**1000)
    # 1366

if __name__ == '__main__':
    main()

