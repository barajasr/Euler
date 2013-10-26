% Problem 68: Magic 5-gon ring
%--------------------------------------------------------------------
% Consider the following "magic" 3-gon ring, filled with the numbers
% 1 to 6, and each line adding to nine.
%
% Working clockwise, and starting from the group of three with the
% numerically lowest external node (4,3,2 in this example), each
% solution can be described uniquely. For example, the above solution
% can be described by the set: 4,3,2; 6,2,1; 5,1,3.
%
% It is possible to complete the ring with four different totals: 9,
% 10, 11, and 12. There are eight solutions in total.
%
% Total   Solution Set
%   9   4,2,3; 5,3,1; 6,1,2
%   9   4,3,2; 6,2,1; 5,1,3
%   10  2,3,5; 4,5,1; 6,1,3
%   10  2,5,3; 6,3,1; 4,1,5
%   11  1,4,6; 3,6,2; 5,2,4
%   11  1,6,4; 5,4,2; 3,2,6
%   12  1,5,6; 2,6,4; 3,4,5
%   12  1,6,5; 3,5,4; 2,4,6
%
% By concatenating each group it is possible to form 9-digit strings;
% the maximum string for a 3-gon ring is 432621513.
%
% Using the numbers 1 to 10, and depending on arrangements, it is
% possible to form 16- and 17-digit strings. What is the maximum
% 16-digit string for a "magic" 5-gon ring?
%--------------------------------------------------------------------
creapList(X, List, Remaining):-
    getElement(X, Head, List, Tail),
    append(Head, Tail, Remaining).

getElement(X, [], [X|Xs], Xs).
getElement(X, [Z|Ys], [Z|Zs], Rest):-
    getElement(X, Ys, Zs, Rest).

gonRing(Sum, Length, Concat):-
    range(10, 1, Range),
    creapList(A, Range, As),
    creapList(B, As, Bs),
    creapList(C, Bs, Cs),
    Sum =:= A + B + C,
    creapList(D, Cs, Ds),
    creapList(E, Ds, Es),
    Sum - C =:= D + E,
    creapList(F, Es, Fs),
    creapList(G, Fs, Gs),
    Sum - E =:= F + G,
    creapList(H, Gs, Hs),
    creapList(I, Hs, Is),
    Sum - G =:= H + I,
    creapList(J, Is, _),
    Sum - I =:= J + B,
    % Start with the smallest external node
    A < D,
    A < F,
    A < H,
    A < J,
    atomic_concat(A, B, AB),
    atomic_concat(AB, C, AC),
    atomic_concat(D, C, DC),
    atomic_concat(DC, E, DE),
    atomic_concat(F, E, FE),
    atomic_concat(FE, G, FG),
    atomic_concat(H, G, HG),
    atomic_concat(HG, I, HI),
    atomic_concat(J, I, JI),
    atomic_concat(JI, B, JB),
    atomic_concat(AC, DE, Concat1),
    atomic_concat(Concat1, FG, Concat2),
    atomic_concat(Concat2, HI, Concat3),
    atomic_concat(Concat3, JB, Concat),
    atom_length(Concat, Length),
    nl, write('Ring 1:'),
    write(A), write(','), write(B), write(','), write(C), nl,
    write('Ring 2:'),
    write(D), write(','), write(C), write(','), write(E), nl,
    write('Ring 3:'),
    write(F), write(','), write(E), write(','), write(G), nl,
    write('Ring 4:'),
    write(H), write(','), write(G), write(','), write(I), nl,
    write('Ring 5:'),
    write(J), write(','), write(I), write(','), write(B), nl.
    
range(End, End, [End]).
range(Start, End, [Start|Rest]):-
    Start > End,
    Next is Start - 1,
    range(Next, End, Rest).

