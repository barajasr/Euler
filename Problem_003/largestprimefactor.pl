% Problem 3: Largest prime factor
%--------------------------------------------------------------------
% The prime factors of 13195 are 5, 7, 13, and 29.
%
% What is the largest prime factor of the number 600851475143?
%--------------------------------------------------------------------
largest_prime(N, Largest):-
    prime_factors(N, List),
    last(List, Largest).

prime_factors(N, List):-
    N > 0,
    prime_factors(N, List, 2), !.

prime_factors(1, [], _).
prime_factors(N, [Factor|List], Factor):-   % N multiple of Factor
    Remainder is N // Factor,
    N =:= Remainder * Factor,
    !, prime_factors(Remainder, List, Factor).
prime_factors(N, List, Factor):-            % N not multiple of Factor
    next_factor(N, Factor, Next),
    prime_factors(N, List, Next).

next_factor(_, 2, 3).
next_factor(N, Factor, Next):-
    Factor * Factor < N,
    !, Next is Factor + 2.
next_factor(N, _, N).                       % Factor > sqrt(N)

% ?- larget_prime(600851475143, X).
% X = 6857.
