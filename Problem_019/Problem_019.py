#! /usr/bin/env python
# -*- coding: iso-8859-15 -*-

# Problem 19: Counting Sundays
#--------------------------------------------------------------------
# You are given the following information, but you may prefer to do
# some research for yourself.
#
#   1 Jan 1900 was a Monday.
#   Thirty days has September,
#   April, June and November.
#   All the rest have thirty-one,
#   Saving February alone,
#   Which has twenty-eight, rain or shine.
#   And on leap years, twenty-nine.
#
# A leap year occurs on any year evenly divisible by 4, but not on
# a century unless it is divisible by 400.
# How many Sundays fell on the first of the month during the 
# twentieth century (1 Jan 1901 to 31 Dec 2000)?
#--------------------------------------------------------------------

from calendar import weekday

# 0m0.031s
def countFirstSundays(startYr, endYr):
    count = 0
    for year in xrange(startYr, endYr+1):
        for month in xrange(1, 13):
            if weekday(year, month, 1) == 6:
                count += 1
    return count

def main():
    print 'Numbers of Sundays falling on the 1st every month from 1901-2000:'
    print countFirstSundays(1901, 2000)
    # 171

if __name__ == '__main__':
    main()

