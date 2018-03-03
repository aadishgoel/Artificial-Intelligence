offspring(X,Y):-parent(Y,X).
ancestor(X,Z):-parent(X,Y);ancestor(Y,Z).	
grandparent(X,Y):-parent(X,Z),parent(Z,Y).
parent(X,Y):-mother(X,Y);father(X,Y).

father(john,tim).
mother(mary,tim).
mother(mary,alex).
father(tim,annie).
father(tim,joe).
sister(annie,joe).
mother(annie,ted).
mother(annie,tom).
father(joe,ben).
