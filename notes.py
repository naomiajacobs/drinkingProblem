import random
from itertools import product
from pprint import pprint
import sys
from typing import List

def pick_another_person(n: int, you: int) -> int:
    # pick a number within N that is not you
    x = random.randint(0, n-1)
    while (x == you):
        x = random.randint(1, n)
    return x

def generate_outcomes(n: int) -> List[List[List[int]]]:
    def helper(outcomes_so_far, you):
        # base case -> len of outcome in outcomes is n
        if you == n:
            print('done')
            return outcomes_so_far
        
        your_choices = [[you, x] for x in range(n) if x != you]
        new_outcomes = [
            outcome_so_far + [choice]
            for outcome_so_far in outcomes_so_far
            for choice in your_choices
        ]
        return helper(new_outcomes, you + 1)


    return helper([[[0, x]] for x in range(n) if x != 0], 1)

def does_everyone_drink(outcome: List[List]) -> bool:
    # sort each tuple in place
    # make a set
    # someone made eye contact if the size of the set is smaller than the original list
    for pair in outcome:
        pair.sort()
    sorted_hashable_outcomes = [tuple(pair) for pair in outcome]
    pprint(sorted_hashable_outcomes)
    pprint(set(sorted_hashable_outcomes))
    return len(set(sorted_hashable_outcomes)) == len(outcome)

def summarize(n: int):
    outcomes = generate_outcomes(n)
    times_everyone_drinks = 0
    for outcome in outcomes:
        outcome.sort()
        everyone_drinks = does_everyone_drink(outcome)
        if everyone_drinks:
            times_everyone_drinks += 1
        pprint(f"{'Everyone drinks' if everyone_drinks else 'Found pairs'}")
    pprint(f"Number of outcomes: {len(outcomes)}")
    pprint(f"Number of times everyone drinks: {times_everyone_drinks}")
    


if __name__ == "__main__":
    # Example usage to see all outcomes for N = 4: `python notes.py 4`
    n = int(sys.argv[1])
    summarize(n)
