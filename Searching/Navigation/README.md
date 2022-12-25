# Navigation

Imagine there is an autonomous agent that likes to fly around the house.

Suppose that a house consists of a grid of N × M cells, represented like this:

	....XXX
	.XXX...
	....X..
	.X.X...
	.X.X.X.
	pX...X@
 
The map consists of N lines (in this case, 6) and M columns (in this case, 7). 
 
Each cell of the house is marked with one of four symbols: 
	 - p : The agent’s current location 
	 - X : A wall through which the agent cannot pass
	 - . : Open space over which the agent can fly 
	 - @ : My location

### Goal:
	Find the shortest path between the agent and myself
	The agent can move one square at a time in any of the four principal compass directions 
	The program should find the shortest distance between the two points and then output a string of letters (L, R, D, and U for left, right, down, and up) indicating that solution
	Program takes a single command line argument, which is the name of the file containing the map file

	e.g.:
	python3 route_pichu.py map1.txt 
	Shhhh... quiet while I navigate!
	Here’s the solution I found:
	16 UUURRDDDRRUURRDD

	Assumption:
	There is always exactly one p and one @ in the map file

	If there is no solution, program will display path length -1 and not display a path

### Abstraction of the program:

#### Valid States:
	A state that has the Pichu in a valid position marked by '.' or '@: Goal position'. It cannot be on walls i.e. 'X'

#### Initial State:
	Pichu is placed at a particular location on the map marked by 'p'
	Walls are at fixed positions marked by 'X'
	My location is marked by '@'

#### Successor Function:
	Move the pichu to valid positions within the map marked by '.'
	These positions can be in four directions: Left, Right, Up, Down
	Different subsets of these are possible depending on the validity

#### Goal State Definition:
	Pichu has reached my position marked by '@' by following the shortest path possible

#### Cost Function:
	Each step costs 1, so the total cost will be the total number of steps in the path

