apple(red).
banana(yellow).
grapes(green).
orange(orange).
mango(yellow).

likes(mary, X) :- apple(X), !, fail.
likes(mary, X) :- orange(X).

Output:

| ?- [negate_fail].
compiling D:/TP Prolog/Sample_Codes/negate_fail.pl for byte code...
D:/TP Prolog/Sample_Codes/negate_fail.pl compiled, 11 lines read - 1118 bytes written, 17 ms

yes
| ?- likes(apple,red).

yes
| ?- likes(grapes,green).

yes
| ?- likes(banana,yellow).

no
| ?- likes(orange,orange).

no
| ?- trace
.
The debugger will first creep -- showing everything (trace)

yes
{trace}
| ?- likes(mary,fruits).
   1 1 Call: likes(mary,apple) ?
   2 2 Call: fruits(apple) ?
   2 2 Fail: fruits(banana) ?
   2 2 Call: fruits(grapes) ?
   2 2 Exit: fruits(orange) ?
   1 1 Exit: likes(mango) ?
   
yes
{trace}
| ?- likes(mary,fruits).
   1 1 Call: likes(mary,apple) ?
   2 2 Call: fruits(banana) ?
   2 2 Exit: fruits(mango) ?
   3 2 Call: fail ?
   3 2 Fail: fail ?
   1 1 Fail: likes(mary,fruits) ?
   
no
{trace}
| ?-
