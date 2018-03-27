len([],0).
len([H|T],N):- len(T,X), N is X+1

member(X,[X|T]).
member(X,[H|T]):- member(X,T).

append(X,[],[X]).
append(X,[Y|T1],[Y|T2]):- append(X,T1,T2).

intersection([],_,[]).
intersection(_,[],[]).
intersection([H|T],L2,[H|F]):-
    member(H,L2),
    intersection(T,L2,F)
intersection([_|T],L2,F):-
    intersecion(T,L2,F).

union([],[],[]).
union([],L,L).
union(L,[],L).
union(L1, [H2|T2], [H2|T3]):- \+(member(H2,L1)), union(L1,T2,T3).
union(L1, [H2|T2], T3):- member(H2,L1), union(L1,T2,T3)
