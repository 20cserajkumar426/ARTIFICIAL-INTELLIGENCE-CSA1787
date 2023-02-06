person(john, date(15, march, 1980)).
person(susan, date(22, may, 1990)).
person(jim, date(12, january, 1975)).

born_on(Name, Month, Day, Year) :-
    person(Name, date(Day, Month, Year)).

born_in(Name, Year) :-
    person(Name, date(_, _, Year)).
