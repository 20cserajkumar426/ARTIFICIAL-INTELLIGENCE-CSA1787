studies(charlie, csc135). // charlie studies csc135
studies(olivia, csc135). // olivia studies csc135
studies(jack, csc131). // jack studies csc131
studies(arthur, csc134). // arthur studies csc134
teaches(kirke, csc135). // kirke teaches csc135
teaches(collins, csc131). // collins teaches csc131
teaches(collins, csc171). // collins teaches csc171
teaches(juniper, csc134). // juniper teaches csc134
Rules
professor(X, Y) :- teaches(X, C),
studies(Y, C).
// X is a professor of Y if X teaches C and Y studies
C.
(here X is a professor, Y is a student and C is a
course and X, Y, C are variables)
Queries / Goals & answers
?- studies(charlie, What).
What = csc135.
// charlie studies what? OR What does charlie
study?
Answer : csc135.
Explanation : Here in query 'What' is a variable
since it starts from uppercase letter. Again prolog
will match the values from given prolog database in
top-down manner and it will check the query from
left-to-right. First, it will find the predicate studies,
then charlie and if any value for 'What' variable
would be matched then variable binding will occur.
As per that prolog will return 'What = csc135' as an
answer to the query.
?- professor(kirke, Students).
Students = charlie;
Students = olivia.
