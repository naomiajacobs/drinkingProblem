Here are the rules to the drinking game:
- everyone puts their head down
- on the count of three, everyone looks up at someone else in the group
- if your selected person is also looking at you, you both drink
- if there are no pairs, everyone drinks

The question is: given a group size N, what is the probability that you drink?

The answer is the sum of two probabilities:
1. What is the probability that you make eye contact with someone else?
2. What is the probability that everyone drinks because no one makes eye contact?

Theoretically deriving the answer to question 1 is trivial - the answer is `1/(n-1)`.
Theoretically deriving the answer to question 2 is hard. Instead, this script simply enumerates all possible options for a group of size N and calculates the probability.

The empirically derived answers for small Ns is:

|   |   |
|---|---|
|   |   |
