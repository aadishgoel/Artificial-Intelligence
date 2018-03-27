solution(_, []).
solution(N, [X/Y|Others]) :-
    solution(N, Others),
    between(1, N, Y),
    noattack(X/Y, Others).

noattack(_,[]).
noattack(X/Y, [X1/Y1 | Others]) :-
    Y =\= Y1,       
    Y1-Y =\= X1-X,  
    Y1-Y =\= X-X1,
    noattack( X/Y, Others).

%solution(8, [1/C1, 2/C2, 3/C3, 4/C4, 5/C5, 6/C6, 7/C7, 8/C8]).
