% Problem 6: Sum square difference
%--------------------------------------------------------------------
% The sum of the squares of the first ten natural numbers is,
%   1² + 2² + ... + 10² = 385
% The square of the sum of the first ten natural numbers is,
%   (1 + 2 + ... + 10)² = 55² = 3025
% Hence the difference between the sum of the squares of the first
% ten natural numbers and the square of the sum is 3025 - 385 = 2640.
%
% Find the difference between the sum of the squares of the first
% one hundred natural numbers and the square of the sum.
%--------------------------------------------------------------------
sum_square_difference(N, Difference):-
    N > 0,
    range(N, Range),
    sum(Range, Sum, SumOfSquares),
    Difference is Sum**2 - SumOfSquares.

range(N, Range):-
    N > 0,
    range(1, N, Range).

range(N, N, [N]):- !.
range(Cnt, N, [Cnt|Rest]):-
    Cnt < N,
    NewCnt is Cnt+1,
    range(NewCnt, N, Rest).

% List, Summation, Summation of Squares
sum([], 0, 0).
sum([N|Ns], Sum, SumSquares):-
    sum(Ns, SubSum, SubSumSquares),
    Sum is SubSum + N,
    SumSquares is SubSumSquares + N**2.

% ?- sum_square_difference(100, Diff).
% Diff = 25164150.

