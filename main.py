import random
from itertools import product
from pprint import pprint
import sys
from typing import List, Tuple

def pick_another_person(n: int, you: int) -> int:
    # pick a number within N that is not you
    x = random.randint(0, n-1)
    while (x == you):
        x = random.randint(1, n)
    return x

def generate_outcomes(n: int) -> List[List[Tuple[int]]]:
    def helper(outcomes_so_far, you):
        if you == n:
            return outcomes_so_far
        
        # pre-sort tuples to make comparison later easier
        your_choices = [(you, x) if you < x else (x, you) for x in range(n) if x != you]
        new_outcomes = [
            outcome_so_far + [choice]
            for outcome_so_far in outcomes_so_far
            for choice in your_choices
        ]
        return helper(new_outcomes, you + 1)


    return helper([[(0, x)] for x in range(n) if x != 0], 1)

def no_pairs(outcome: List[Tuple[int]]) -> bool:
    # make a set
    # someone made eye contact if the size of the set is smaller than the original list
    return len(set(outcome)) == len(outcome)

def format_probability(p: float):
    return f"{round(p*100, 2)}%"

def summarize(max: int):
    for n in range(3, max + 1):
        outcomes = generate_outcomes(n)
        times_no_pairs = 0
        for outcome in outcomes:
            if no_pairs(outcome):
                times_no_pairs += 1
        p_no_pairs = times_no_pairs/len(outcomes)
        p_you_make_eye_contact = 1/(n-1)
        p_you_drink = p_no_pairs + p_you_make_eye_contact
        print(f"| {n} | {len(outcomes)} | {times_no_pairs} | {format_probability(p_no_pairs)} | {format_probability(p_you_make_eye_contact)} | {format_probability(p_you_drink)} |")


if __name__ == "__main__":
    # Example usage to see all outcomes up to N = 4: `python notes.py 4`
    n = int(sys.argv[1])
    summarize(n)
