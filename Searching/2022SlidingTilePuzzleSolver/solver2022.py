#!/usr/local/bin/python3
# solver2022.py : 2022 Sliding tile puzzle solver
#
# Code by: Dheeraj Manchandia
#
# Based on skeleton code by D. Crandall & B551 Staff, Fall 2022
#

import sys
import numpy as np
ROWS=5
COLS=5

def printable_board(board):
    return [ ('%3d ')*COLS  % board[j:(j+COLS)] for j in range(0, ROWS*COLS, COLS) ]


def make_nested(state):
    
    s = []
    i = 0
    while i < ROWS*COLS:
        s.append(list(state[i:i+COLS]))
        i = i + COLS
    
    return(s) 
    
def merge_nested(state):
    
    s = []

    for x in range(len(state)):
        for y in range(len(state[x])):
            s.append(state[x][y])
        
    return(s)

def move_left(state,r):
    
    temp = state.copy()
    temp[r] = temp[r][1:] + temp[r][:1]
    return(temp)

def move_right(state,r):
    
    temp = state.copy()
    temp[r] = temp[r][-1:] + temp[r][:-1]
    return(temp)

def transpose(state):
    
    return ([list(c) for c in zip(*state)])

def rotate_right(state,r,residual):
    
    state[r] = [state[r][0]] +[residual] + state[r][1:]
    residual = state[r].pop()
    return(residual)

def rotate_left(state,r,residual):
    
    state[r] = state[r][:-1] + [residual] + [state[r][-1]]
    residual = state[r].pop(0)
    return(residual)

def move_clockwise(state):
    
    temp = state.copy()
    temp[0]=[temp[1][0]]+temp[0]
    residual=temp[0].pop()
    temp=transpose(temp)
    residual=rotate_right(temp,-1,residual)
    temp=transpose(temp)
    residual=rotate_left(temp,-1,residual)
    temp=transpose(temp)
    residual=rotate_left(temp,0,residual)
    temp=transpose(temp)
    return temp

def move_cclockwise(state):

    temp = state.copy()
    temp[0]=temp[0]+[temp[1][-1]]
    residual=temp[0].pop(0)
    temp=transpose(temp)
    residual=rotate_right(temp,0,residual)
    temp=transpose(temp)
    residual=rotate_right(temp,-1,residual)
    temp=transpose(temp)
    residual=rotate_left(temp,-1,residual)
    temp=transpose(temp)
    return temp

# return a list of possible successor states
def successors(state, path, v, fringe):
    
    f_s = [x[0][1] for x in fringe]
    
    state = make_nested(state)
    succ_states = []
    
    #print("Visited:",v)
    
    #print("Right")
    for i in range(ROWS):
        succ = move_right(state, i)
        succ = merge_nested(succ)
        if tuple(succ) not in v and tuple(succ) not in f_s:
            succ_states.append(((len(path) + (h(tuple(succ))/COLS),(tuple(succ))),"R"+str(i+1)))
    
    #print("Left")
    for i in range(ROWS):
        succ = move_left(state, i)
        succ = merge_nested(succ)
        if tuple(succ) not in v and tuple(succ) not in f_s:
            succ_states.append(((len(path) + (h(tuple(succ))/COLS),(tuple(succ))),"L"+str(i+1)))
        
    #print("Up")
    for i in range(COLS):
        succ = transpose(move_left(transpose(state), i))
        succ = merge_nested(succ)
        if tuple(succ) not in v and tuple(succ) not in f_s:
            succ_states.append(((len(path) + (h(tuple(succ))/ROWS),(tuple(succ))),"U"+str(i+1)))
        
    #print("Down")
    for i in range(COLS):
        succ = transpose(move_right(transpose(state), i))
        succ = merge_nested(succ)
        if tuple(succ) not in v and tuple(succ) not in f_s:
            succ_states.append(((len(path) + (h(tuple(succ))/ROWS),(tuple(succ))),"D"+str(i+1)))
    
    #print("OC")
    succ = move_clockwise(state)
    succ = merge_nested(succ)
    if tuple(succ) not in v and tuple(succ) not in f_s:
        succ_states.append(((len(path) + (h(tuple(succ))/16),(tuple(succ))),"Oc"))
    
    #print("OCC")
    succ = move_cclockwise(state)
    succ = merge_nested(succ)
    if tuple(succ) not in v and tuple(succ) not in f_s:
        succ_states.append(((len(path) + (h(tuple(succ))/16),(tuple(succ))),"Occ"))
    
    #print("IC")
    succ = np.array(state)
    inner = succ[1:-1,1:-1].tolist()
    inner = move_clockwise(inner)
    succ[1:-1,1:-1] = np.array(inner)
    succ = succ.tolist()
    succ = merge_nested(succ)
    if tuple(succ) not in v and tuple(succ) not in f_s:
        succ_states.append(((len(path) + (h(tuple(succ))/8),(tuple(succ))),"Ic"))
    
    #print("ICC")
    succ = np.array(state)
    inner = succ[1:-1,1:-1].tolist()
    inner = move_cclockwise(inner)
    succ[1:-1,1:-1] = np.array(inner)
    succ = succ.tolist()
    succ = merge_nested(succ)
    if tuple(succ) not in v and tuple(succ) not in f_s:
        succ_states.append(((len(path) + (h(tuple(succ))/8),(tuple(succ))),"Icc"))
    
    
    #print(len(succ_states))
    #print(succ_states)
    
    return succ_states

# check if we've reached the goal
def is_goal(state):
    return state == tuple(range(1,(ROWS*COLS) + 1 ))

# Heuristic function:
# given a state, return an estimate of the number of steps to a goal from that state
def h(state):
#     mp_c = 0
#     for i in range(len(state)):
#         if not state[i] == i + 1:
#             mp_c = mp_c + 1
    
#     return mp_c

    c = 0
    for i in range(1,len(state)+1):
        c = c + (abs(state.index(i) + 1 -i))
    
#     p = {
#         (1,2,3,4,5,6,7):0,
#         (8,9,10,11,12,13):0,
#         (14,15,16,17,18,19):0,
#         (20,21,22,23,24,25):0
#     }

#     for key,values in p.items():

#         d = 0

#         for i in range(len(key)):
#             #print(key[i])
#             #print(state.index(key[i]))
#             d = d + abs(state.index(key[i]) - key[i])

#         p[key] = d

#     return(sum(p.values()))

    return c
    

def solve(initial_board):
    
    fringe = []
        
    fringe += [((h(initial_board),initial_board), [])]
        
    v = []
    
    while len(fringe) > 0:
        fringe.sort()
        #print(fringe)
        
        ((p,state), path) = fringe.pop(0)
        
        #print(((p,state), path))
        
        v.append(state)
        
        if is_goal(state):
            return path
    
        for s in successors(state,path,v,fringe):
            fringe.append((s[0], path + [s[1]] ))
    
    
    return []


if __name__ == "__main__":
    if(len(sys.argv) != 2):
        raise(Exception("Error: expected a board filename"))

    start_state = []
    with open(sys.argv[1], 'r') as file:
        for line in file:
            start_state += [ int(i) for i in line.split() ]

    if len(start_state) != ROWS*COLS:
        raise(Exception("Error: couldn't parse start state file"))

    print("Start state: \n" +"\n".join(printable_board(tuple(start_state))))

    print("Solving...")
    route = solve(tuple(start_state))
    
    print("Solution found in " + str(len(route)) + " moves:" + "\n" + " ".join(route))
