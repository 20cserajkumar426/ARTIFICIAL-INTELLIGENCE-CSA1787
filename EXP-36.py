% Define the state space as a list of nodes
state_space([a, b, c, d, e, f, g]).

% Define the initial state
initial_state(a).

% Define the goal state
goal_state(g).

% Define the heuristic function
heuristic(Node, Value) :- 
    (Node == g -> Value is 0;
     Node == a -> Value is 2;
     Node == b -> Value is 3;
     Node == c -> Value is 4;
     Node == d -> Value is 5;
     Node == e -> Value is 5;
     Node == f -> Value is 6).

% Define the transitions between states
transition(a, b, 1).
transition(a, c, 2).
transition(b, d, 3).
transition(b, e, 1).
transition(c, f, 4).
transition(c, g, 2).
transition(d, e, 2).
transition(d, f, 3).
transition(e, g, 4).
transition(f, g, 1).

% Define the best_first_search predicate
best_first_search :-
    initial_state(Initial),
    goal_state(Goal),
    best_first([[Initial]], Goal).

% Define the best_first predicate, which does the actual search
best_first([[Node|Path]|_], Goal) :-
    Node == Goal,
    write('Path is '), write([Node|Path]), nl.

best_first([Path|Queue], Goal) :-
    extend(Path, NewPaths),
    append(Queue, NewPaths, Queue1),
    sort_queue(Queue1, NewQueue),
    best_first(NewQueue, Goal).

% Define the extend predicate, which generates new paths by exploring
% transitions from the current state
extend([Node|Path], NewPaths) :-
    findall([NextNode, Node|Path], (transition(Node, NextNode, _), not(member(NextNode, Path))), NewPaths).

% Define the sort_queue predicate, which sorts the queue of paths based on the
% heuristic value of the last node in the path
sort_queue(Queue, SortedQueue) :-
    sort(Queue, SortedQueue, @compare_heuristic).

compare_heuristic([A|_], [B|_]) :-
    heuristic(A, ValueA),
    heuristic(B, ValueB),
    compare(Order, ValueA, ValueB),
    Order = '>'.
