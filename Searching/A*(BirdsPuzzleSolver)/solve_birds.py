#!/usr/local/bin/python3
# solve_birds.py : Bird puzzle solver
#
# Code by: Dheeraj Manchandia
#
# Based on skeleton code by D. Crandall & B551 course staff, Fall 2022
#
# N birds stand in a row on a wire, each wearing a t-shirt with a number.
# In a single step, two adjacent birds can swap places. How can
# they rearrange themselves to be in order from 1 to N in the fewest
# possible steps?

# !/usr/bin/env python3
import sys
N=5

# Goal state:
# given a state, returns True or False to indicate if it is the goal state
def is_goal(state):
    return state == list(range(1, N+1))

# Successor function:
# given a state, return a list of successor states
def successors(state,path):
    
    succ = [ state[0:n] + [state[n+1],] + [state[n],] + state[n+2:] for n in range(0, N-1) ]
    final_succ = []
    
    for x in succ:
        if x not in path:
            final_succ.append((len(path)+h(x),x))
    
    return final_succ

# Heuristic function:
# given a state, return an estimate of the number of steps to a goal from that state
def h(state):
    mp_c = 0
    for i in range(len(state)):
        if not state[i] == i + 1:
            mp_c = mp_c + 1
    
    return mp_c

#########
#
# THE ALGORITHM:
#
#
def solve(initial_state):
    fringe = []

    fringe += [((h(initial_state),initial_state), []),]
    
    while len(fringe) > 0:
        fringe.sort()
        #print("Fringe\n", fringe)
        ((p,state), path) = fringe.pop(0)
        
        if is_goal(state):
            return path+[state,]

        for s in successors(state,path):
            fringe.append((s, path+[state,]))

    return []


if __name__ == "__main__":
    if(len(sys.argv) != 2):
        raise(Exception("Error: expected a test case filename"))

    test_cases = []
    with open(sys.argv[1], 'r') as file:
        for line in file:
            test_cases.append([ int(i) for i in line.split() ])
    for initial_state in test_cases:
        	print('From state ' + str(initial_state) + " found goal state by taking path: " + str(solve(initial_state)))


