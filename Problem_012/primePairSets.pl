% Problem 12: Highly divisible triangular number
%--------------------------------------------------------------------
% The primes 3, 7, 109, and 673, are quite remarkable. By taking any
% two primes and concatenating them in any order the result will always
% be prime. For example, taking 7 and 109, both 7109 and 1097 are prime.
% The sum of these four primes, 792, represents the lowest sum for a
% set of four primes with this property.
%
% Find the lowest sum for a set of five primes for which any two primes
% concatenate to produce another prime.
%-------------------------------------------------------------------
primePairSets([Prime0, Prime1, Prime2, Prime3, Prime4], Sum):-
    genPrimes(19000, Primes),
    creapList(Prime0, Primes, Rest),
    creapList(Prime1, Rest, Rest1),
    creapList(Prime2, Rest1, Rest2),
    creapList(Prime3, Rest2, Rest3),
    creapList(Prime4, Rest3, _),
    %write(Prime0), write(','), write(Prime1), write(','),
    %write(Prime2), write(','), write(Prime3), write(','),
    %write(Prime4), nl,
    concatPrimes([Prime0, Prime1, Prime2, Prime3, Prime4]),
    Sum is Prime0 + Prime1 + Prime2 + Prime3 + Prime4.

creapList(X, [X|Xs], Xs).
creapList(X, [_|Ys], Rest):-
    creapList(X, Ys, Rest).

concatPrimes([]):- !.
concatPrimes([X|Xs]):-
    concatPrimes(X, Xs),
    concatPrimes(Xs).

concatPrimes(_, []):- !.
concatPrimes(X, [Y|Ys]):-
    atomic_concat(X, Y, Test1),
    atomic_concat(Y, X, Test2),
    atom_number(Test1, N1),
    atom_number(Test2, N2),
    %write(X), write(','), write(Y),
    %write(':'), write(N1), write(':'), write(N2), nl,
    isPrime(N1),
    isPrime(N2),
    concatPrimes(X, Ys).

genPrimes(EndRange, Primes):-
    genPrimes(3, EndRange, Primes), !.

genPrimes(Cnt, EndRange, []):-
    Cnt > EndRange, !.
genPrimes(Cnt, EndRange, [Cnt|Primes]):-
    Cnt =< EndRange,
    isPrime(Cnt),
    nextCandidate(Cnt, NewCnt),
    genPrimes(NewCnt, EndRange, Primes).
genPrimes(Cnt, EndRange, Primes):-
    Cnt =< EndRange,
    nextCandidate(Cnt, NewCnt),
    genPrimes(NewCnt, EndRange, Primes).

nextCandidate(2, 3).
nextCandidate(N, Next):-
    N >= 3,
    Next is N + 2.

isPrime(N):-
    prime(N), !.

:- dynamic prime/1.
prime(2):- !.
prime(3):- !.
prime(N):-
    N > 3,
    N mod 2 =\= 0,
    \+ divisible(N, 3),
    asserta((prime(N):- !)).

divisible(N, I):-
    N mod I =:= 0.
divisible(N, I):-
    I*I < N,
    nextCandidate(I, NewI),
    divisible(N, NewI).

