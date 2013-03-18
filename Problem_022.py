#! usr/bin/env python
# -*- coding: iso-8859-15 -*-

# Problem 22: Name Scores
#--------------------------------------------------------------------
# Using names.txt (right click and 'Save Link/Target As...'), a 46K
# text file containing over five-thousand first names, begin by
# sorting it into alphabetical order. Then working out the
# alphabetical value for each name, multiply this value by its
# alphabetical position in the list to obtain a name
# score.
#
# For example, when the list is sorted into alphabetical order, COLI,
# which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in
# the list. So, COLIN would obtain a score of 938  53 = 49714.
#
# What is the total of all the name scores in the file?
#--------------------------------------------------------------------

values = {char:value+1 for (value, char) in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZ')}

def nameScores(filename):
    totalScore, n = (0, 0)
    contents = open(filename).read().replace('"', '').split(',')
    contents.sort()
    for name in contents:
        n += 1
        score = 0
        for char in name:
            score += values[char]
        totalScore += score*n
    return totalScore

# 0m0.038s
def main():
    print 'Total of name scores from file:'
    print nameScores('names.txt')
    # 871198282

if __name__ == '__main__':
    main()

