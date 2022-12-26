# Birds, heuristics, and A*

On a power line sit five birds, each wearing a different number from 1 to N. 

### Goal:
    They start in a random order and their goal is to re-arrange themselves to be in order from 1 to N (e.g., 12345), in as few steps as possible
    In any one step, exactly one bird can exchange places with exactly one of its neighboring birds
    
This is a search problem in which there is a set of states S corresponding to all possible permutations of the birds (i.e., S = {12345, 12354, 12453, ...} for N = 5)

### The program:
    1. Uses a priority queue.
    2. Implements an admissible heuristic h(s).
    3. For the priority value, used f(s) = g(s) + h(s), where g(s) is the cost from the initial state to s


