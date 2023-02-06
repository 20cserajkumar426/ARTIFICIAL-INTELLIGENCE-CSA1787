bird(eagle).
bird(penguin).
can_fly(penguin):-!,fail.
can_fly(X):-bird(X).
