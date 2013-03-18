#! usr/bin/env python
# -*- coding: iso-8859-15 -*-

# Problem 39: Integer right triangles
#--------------------------------------------------------------------
# If p is the perimeter of a right angle triangle with integral
# length sides, {a,b,c}, there are exactly three solutions for 
# p = 120.
#   {20,48,52}, {24,45,51}, {30,40,50}
# For which value of p ≤ 1000, is the number of solutions maximised?
#--------------------------------------------------------------------
    
# combine with Problem 9
# · a² + b² = c²
# · a + b + c = p
# ∴ a² + b² = (p-a-b)²
#           = p² + a² + b² - 2pa - 2pb + 2ab
#       0   = p² - 2pa - 2pb + 2ab
#   2pb-2ab = p² - 2pa
#  b(2p-2a) = p² - 2pa
#   · b = (p² -2pa) / (2p-2a)
#
# 0m0.197s
def rightTriangleSets():
    solution, maxSolution = 0, 0
    for p in xrange(12, 1000):
        solutions = 0
        # 3,4,5 triange 12/3 = 4
        for a in xrange(1, p/3):
            b = (p*p - 2*p*a) / (2*p - 2*a)
            if b <= 0:
                break
            c = p-a-b
            if a*a + b*b == c*c:
                solutions += 1
        if solutions > maxSolution:
            maxSolution = solutions
            solution = p
    return solution

def main():
    print 'For which value of p ≤ 1000, is the number of solutions' +\
          ' maximized when considering right triangles'
    print rightTriangleSets()
    # 840

if __name__ == '__main__':
    main()

