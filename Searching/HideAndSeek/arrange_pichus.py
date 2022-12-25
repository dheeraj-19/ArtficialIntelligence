#!/usr/local/bin/python3
#
# arrange_pichus.py : arrange agents on a grid, avoiding conflicts
#
# Submitted by : [NAME: Dheeraj Manchandia AND USERNAME: dmancha]
#
# Based on skeleton code in CSCI B551, Fall 2022.

import sys

# Parse the map from a given filename
def parse_map(filename):
	with open(filename, "r") as f:
		return [[char for char in line] for line in f.read().rstrip("\n").split("\n")][3:]

# Count total # of pichus on house_map
def count_pichus(house_map):
    return sum([ row.count('p') for row in house_map ] )

# Return a string with the house_map rendered in a human-pichuly format
def printable_house_map(house_map):
    return "\n".join(["".join(row) for row in house_map])

# Add a pichu to the house_map at the given position, and return a new house_map (doesn't change original)
def add_pichu(house_map, row, col):
    return house_map[0:row] + [house_map[row][0:col] + ['p',] + house_map[row][col+1:]] + house_map[row+1:]

def find_blocked(house_map):

    blocked = []

    # Logic to find all the blocked positions based on pichus locations

    for pichu in [(row_i,col_i) for col_i in range(len(house_map[0])) for row_i in range(len(house_map)) if house_map[row_i][col_i]=="p"]:
        
        # Block all positions from pichu to top of the map in same column till a wall is encountered
        for i in range(pichu[0], -1, -1):
            if house_map[i][pichu[1]] == 'X' or house_map[i][pichu[1]] == '@':
                break
            if (i,pichu[1]) not in blocked and house_map[i][pichu[1]] == '.':
                blocked.append((i,pichu[1]))

        # Block all positions from pichu to bottom of the map in same column till a wall is encountered
        for i in range(pichu[0],len(house_map)):
            if house_map[i][pichu[1]] == 'X' or house_map[i][pichu[1]] == '@':
                break
            if (i,pichu[1]) not in blocked and house_map[i][pichu[1]] == '.':
                blocked.append((i,pichu[1]))

        # Block all positions from pichu to top of the map in same row till a wall is encountered
        for i in range(pichu[1],-1,-1):
            if house_map[pichu[0]][i] == 'X' or house_map[pichu[0]][i] == '@':
                break
            if (pichu[0],i) not in blocked and house_map[pichu[0]][i] == '.':
                blocked.append((pichu[0],i))

        # Block all positions from pichu to bottom of the map in same column till a wall is encountered
        for i in range(pichu[1],len(house_map[0])):
            if house_map[pichu[0]][i] == 'X' or house_map[pichu[0]][i] == '@':
                break
            if (pichu[0],i) not in blocked and house_map[pichu[0]][i] == '.':
                blocked.append((pichu[0],i))

        # Block all positions from pichu to north-east diagoal till a wall is encountered or map ends
        for i in range(pichu[0],-1,-1):
            if (pichu[1]+abs(i-pichu[0])) >= len(house_map[0]):
                break
            if house_map[i][pichu[1]+abs(i-pichu[0])] == 'X' or house_map[i][pichu[1]+abs(i-pichu[0])] == '@':
                break
            if (i,(pichu[1]+abs(i-pichu[0]))) not in blocked and house_map[i][pichu[1]+abs(i-pichu[0])] == '.':
                blocked.append((i,(pichu[1]+abs(i-pichu[0]))))

        # Block all positions from pichu to north-west diagoal till a wall is encountered or map ends
        for i in range(pichu[0],-1,-1):
            if (pichu[1]-abs(i-pichu[0])) < 0:
                break
            if house_map[i][pichu[1]-abs(i-pichu[0])] == 'X' or house_map[i][pichu[1]-abs(i-pichu[0])] == '@':
                break
            if (i,(pichu[1]-abs(i-pichu[0]))) not in blocked and house_map[i][pichu[1]-abs(i-pichu[0])] == '.':
                blocked.append((i,(pichu[1]-abs(i-pichu[0]))))

        # Block all positions from pichu to south-east diagoal till a wall is encountered or map ends
        for i in range(pichu[0],len(house_map)):
            if (pichu[1]+abs(i-pichu[0])) >= len(house_map[0]):
                break
            if house_map[i][pichu[1]+abs(i-pichu[0])] == 'X' or house_map[i][pichu[1]+abs(i-pichu[0])] == '@':
                break
            if (i,(pichu[1]+abs(i-pichu[0]))) not in blocked and house_map[i][pichu[1]+abs(i-pichu[0])] == '.':
                blocked.append((i,(pichu[1]+abs(i-pichu[0]))))

        # Block all positions from pichu to south-west diagoal till a wall is encountered or map ends
        for i in range(pichu[0],len(house_map)):
            if (pichu[1]-abs(i-pichu[0])) < 0:
                break
            if house_map[i][pichu[1]-abs(i-pichu[0])] == 'X' or house_map[i][pichu[1]-abs(i-pichu[0])] == '@':
                break
            if (i,(pichu[1]-abs(i-pichu[0]))) not in blocked and house_map[i][pichu[1]-abs(i-pichu[0])] == '.':
                blocked.append((i,(pichu[1]-abs(i-pichu[0]))))


    return(len(blocked),blocked)


# Get list of successors of given house_map state
def successors(house_map):
    
    # Find the blocked positions
    b = find_blocked(house_map)
    c = b[0]
    blocked = b[1]
    
    # Create a list with next pichu at available locations
    l = [ add_pichu(house_map, r, c) for r in range(0, len(house_map)) for c in range(0,len(house_map[0])) if (r,c) not in blocked and house_map[r][c] == '.' ]
    
    # If no posible positions return
    if l == []:
        return l

    d = []

    # Logic to find the best next position of the pichu
    # Call the find blocked again for all possible positions and find min number of blocked positions
    # That will be best next step
    for i in range(len(l)):
        t = find_blocked(l[i])
        d.append((t[0],l[i]))

    return [min(d)[1]]
	
# check if house_map is a goal state
def is_goal(house_map, k):
    return count_pichus(house_map) == k 

# Arrange agents on the map
#
# This function MUST take two parameters as input -- the house map and the value k --
# and return a tuple of the form (new_house_map, success), where:
# - new_house_map is a new version of the map with k agents,
# - success is True if a solution was found, and False otherwise.
#
def solve(initial_house_map,k):
    pichu_loc=[(row_i,col_i) for col_i in range(len(initial_house_map[0])) for row_i in range(len(initial_house_map)) if initial_house_map[row_i][col_i]=="p"][0]
    fringe = [initial_house_map]

    while len(fringe) > 0:
        for new_house_map in successors( fringe.pop()):
            if new_house_map == []:
                break
            if is_goal(new_house_map,k):
                return(new_house_map,True) # Return the map and True if a solution is found
            fringe.append(new_house_map)
    
    return(initial_house_map,False) # Return False if no solution found 
# Main Function
if __name__ == "__main__":
    house_map=parse_map(sys.argv[1])
    # This is k, the number of agents
    k = int(sys.argv[2])
    print ("Starting from initial house map:\n" + printable_house_map(house_map) + "\n\nLooking for solution...\n")
    solution = solve(house_map,k)
    print ("Here's what we found:")
    print (printable_house_map(solution[0]) if solution[1] else "False")


