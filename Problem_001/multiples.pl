% Problem 1: Multiples of 3 and 5
%--------------------------------------------------------------------
%   If we list all the natural numbers below 10 that multiples of 3
%   or 5, we get 3, 5, 6 and 9. The sum of thes is 23.
%
%   Find the sum of all the multiples of 3 or 5 below 1000.
%--------------------------------------------------------------------

sum_of_multiples(N, N1, EndRange, Sum):-
    list_of_multiples(N, N, EndRange, List1),
    list_of_multiples(N1, N1, EndRange, List2),
    ord_union(List1, List2, UniqueSet), 
    sum_of_list(UniqueSet, Sum).

list_of_multiples(_, Cnt, EndRange, []):-
    Cnt >= EndRange.
list_of_multiples(N, Cnt, EndRange, [Cnt|Multiples]):-
    Cnt < EndRange,
    NewCnt is Cnt + N,
    list_of_multiples(N, NewCnt, EndRange, Multiples), !.

sum_of_list([], 0).
sum_of_list([X|Xs], Sum):-
    sum_of_list(Xs, SubSum),
    Sum is X + SubSum.

% ?- sum_of_multiples(3,5,1000, Sum).
% Sum = 233168.
