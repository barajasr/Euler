#! /usr/bin/env python
# -*- coding: iso-8859-15 -*-

# Problem 17: Number letter counts
#--------------------------------------------------------------------
# If the numbers 1 to 5 are written out in words: one, two, three,
# four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in
# total.
#
# If all the numbers from 1 to 1000 (one thousand) inclusive were 
# written out in words, how many letters would be used?
#
# NOTE: Do not count spaces or hyphens. For example, 342 (three
# hundred and forty-two) contains 23 letters and 115 (one hundred
# and fifteen) contains 20 letters. The use of "and" when writing
# out numbers is in compliance with British usage.
#--------------------------------------------------------------------

words = {0:0, 1:3, 2:3, 3:5, 4:4, 5:4, 6:3, 7:5, 8:5, 9:4, 10:3,
         11:6, 12:6, 13:8, 14:8, 15:7, 16:7, 17:9, 18:8, 19:8,
         20:6, 30:6, 40:5, 50:5, 60:5, 70:7, 80:6, 90:6, 
         10000:11}

# 0m0.031s
def numberWords(maxN):
    total = 0
    hundredsWidth = 7
    for n in xrange(1, maxN+1):
        if n in words:
            total += words[n]
            continue
        addAnd = False
        hundredths = n/100
        remainder = n%100
        if hundredths > 0:
            total += words[hundredths] + hundredsWidth
            if remainder == 0: continue
            addAnd = True
        if remainder >= 20:
            tenths = remainder/10
            remainder = remainder%10
            total += words[tenths*10]
            total += words[remainder]
        else:
            total += words[remainder]
        if addAnd: total += 3
    return total

def main():
    print 'Length of all numbers [1...1000] spelled out:'
    print numberWords(1000)
    # 21124

if __name__ == '__main__':
    main()

