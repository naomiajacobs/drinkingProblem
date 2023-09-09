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

| N | N(outcomes) | N(everyone drinks) | P(everyone drinks) | P(you make eye contact) | P(you drink) |
|---|-------------|--------------------|--------------------|-------------------------|--------------|
| 3 | 8 | 2 | 25.0% | 50.0% | 75.0% |
| 4 | 81 | 30 | 37.04% | 33.33% | 70.37% |
| 5 | 1024 | 444 | 43.36% | 25.0% | 68.36% |
| 6 | 15625 | 7360 | 47.1% | 20.0% | 67.1% |
| 7 | 279936 | 138690 | 49.54% | 16.67% | 66.21% |
| 8 | 5764801 | 2954364 | 51.25% | 14.29% | 65.53% |
| 9 | 134217728 | 70469000 | 52.5% | 12.5% | 65.0% |
