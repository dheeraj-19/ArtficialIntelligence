# Hide-and-seek

Imagine there are K autonomous agent that likes to fly around the house.

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
The problem is that these agents do not like one another, which means that they have to be positioned such that no two agents can see one another

### Assumptions:
	- k ≥ 1
	- Two agents can see each other if they are on either the same row, column, or diagonal of the map, and there are no walls between them
	- An agent can only be positioned on empty squares (marked with .)
	- It’s okay if agents see me, and I obscure the view between agents, as a wall
	- Exactly one p will already be fixed in the input map file

Program should output a new version of the map, but with the agents’ locations marked with p

If there is no solution, program should displays False

#### e.g.:
	python3 arrange_pichus.py map1.txt 5
	 ....XXX
	 .XXXp..
	 .p..X..
	 .X.X...
	 .X.X.Xp
	 pX.p.X@
	 
### Abstraction of the program:

#### Valid States:
	Any arrangement of 1 to K Pichu's in the map placed on positions marked by '.', such that no to Pichu's can see each other
	They cannot be on walls i.e. 'X' and '@'
	If they are in the same row, column, or diagonal they need to separated by a wall 'X'

#### Initial State:
	1 Pichu is placed at a particular location in the map marked by 'p'
	Walls are at fixed positions marked by 'X'
	My location marked by '@'

#### Goal State Definition:
	All K pichus are placed on the map, such that no to Pichu's can see each other

#### Cost Function:
	1 for placing each queen from 2 to K
	
#### Successor Function:
	Place the next pichu on valid positions within the map marked by '.'
	This position is derived by considering all the possible positions open for that pichu
	The final positions is decided based on the minimum numbers of blocked positions that will result after placing the new pichu

#### Solution
	To add constraints, I created a list: blocked
	For every Pichu placed in the map I place the co-ordinates of all the blocked positions into this list.
	Then while considering the next position, I check this blocked list to decide the final position to place the pichu on.
	Also, all these possible states are getting stored in the fringe.

	Now to find the blocked positions, I need to check:
	-Positions in the same row to the left of Pichu location
	-Positions in the same row to the right of Pichu location
	-Positions in the same column above Pichu location
	-Positions in the same column below of Pichu location
	-Positions in the diagonals on all four sides of Pichu location
	All these should be blocked till we encounter an 'X'

	If there is no solution possible then once the fringe is empty it will return 'False'.

	This solution worked well but the pattern was different

	Then, I tested 1 case whihc was failing

	So, I worked on improving the sucessor function.
	One point was that the fringe was storing all possible positions till the very end.
	This is not needed as once a pichu is placed we can clear it, we don't really have to trace back the path

	Then, to find the best possible position to place the pichu, I updated the successor function.
	Instead of checking the available positions and blocked positions.
	I calculate the number of blocked positions for each next state.
	Find the minimum number of blocked positions and choose that as the next position to place the Pichu on.
