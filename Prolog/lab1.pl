fib(0,0).
fib(1,1).
fib(N,Z):-N>1,N1 is N-1,N2 is N-2,fib(N1,X),fib(N2,Y),Z is X+Y.


/* Output
?- fib(0,What).
What = 0 .
?- fib(1,What).
What = 1 .
?- fib(2,What).
What = 1 .
?- fib(3,What).
What = 2  
*/


tempCF(C,F):- F is (C*1.8)+32.
tempFC(F,C):- C is (F-32)*0.556.

/* Output
?- tempCF(-40,What).
What = -40.0.
?- tempFC(32,What).
What = 0.0.
?- tempCF(37,What).
What = 98.60000000000001.
*/

