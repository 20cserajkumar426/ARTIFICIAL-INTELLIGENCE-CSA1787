%% Define the knowledge base
:- dynamic fact/1.
fact(a).
fact(b).
fact(e).

rule(r1, [a], c).
rule(r2, [b], d).
rule(r3, [c,d], e).

% Define the backward chaining predicate
backward_chain(X) :-
    fact(X).

backward_chain(X) :-
    rule(Rule, _, X),
    backward_chain_premises(Rule).

% Define the backward_chain_premises predicate
backward_chain_premises(Rule) :-
    rule(Rule, Premises, _),
    check_premises(Premises).

% Define the check_premises predicate
check_premises([]).

check_premises([Premise|Rest]) :-
    backward_chain(Premise),
    check_premises(Rest).

% Queries
ask(X):- backward_chain(X),write(X), nl.
ask_not(X):- \+backward_chain(X), write(X), nl.
