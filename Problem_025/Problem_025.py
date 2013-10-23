#! usr/bin/env python
# -*- coding: iso-8859-15 -*-

# Problem 25: 1000-Digit Fibonacci number
#--------------------------------------------------------------------
# The Fibonacci sequence is defined by the recurrence relation:
#
# Fn = Fn1 + Fn2, where F1 = 1 and F2 = 1.
# Hence the first 12 terms will be:
#
#   F₁ = 1
#   F₂ = 1
#   F₃ = 2
#   F₄ = 3
#   F₅ = 5
#   F₆ = 8
#   F₇ = 13
#   F₈ = 21
#   F₉ = 34
#   F₁₀ = 55
#   F₁₁ = 89
#   F₁₂ = 144
#   The 12th term, F12, is the first term to contain three digits.
#
# What is the first term in the Fibonacci sequence to contain 1000
# digits?
#--------------------------------------------------------------------

'''
Of note, via MathBlog:
Fibonacci numbers converge to:
    Fib(n) = φⁿ/√5, rounded to nearest int
    ∴ find n ∈ N s.t. 
        φⁿ/√5 > 10**999
    log of sides
        log(φ)*n-log(5)/2 > log(10)*999
    move n
        n > (log(10)*999 + log(5)/2)/log(φ) ≌ 4781.59
'''

fib = {1:1, 2:1}

def fibOfLength(n):
    if n == 1:
        return 1
    i = len(fib)
    result = str(fib[i])
    while len(result) < n:
        i += 1
        fib[i] = fib[i-1]+fib[i-2]
        result = str(fib[i])
    return i

# 0m0.094s
def main():
    print 'What is the first term in the Fibonacci sequence to' +\
          ' contain 1000 digits?'
    print fibOfLength(1000)
    # 4782

if __name__ == '__main__':
    main()

