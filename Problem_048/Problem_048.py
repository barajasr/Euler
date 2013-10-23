#! usr/bin/env python
# -*- coding: iso-8859-15 -*-

# Problem 48: Self Powers
#--------------------------------------------------------------------
#The series, 1¹ + 2² + 3³ + ... + 10¹⁰ = 10405071317.
#
# Find the last ten digits of the series, 
# 1¹ + 2² + 3³ + ... +1000¹⁰⁰⁰
#--------------------------------------------------------------------

def lastFour(limit):
    # only last 10 digits matter
    return sum([(n**n)%(10**10) for n in xrange(1, limit+1)])%(10**10)

def main():
    print 'The last ten digits of 1¹+....1000¹⁰⁰⁰.'
    print lastFour(1000)
    # 9110846700

if __name__ == '__main__':
    main()

