# Raichu Game

Raichu is a popular childhood game played on an n × n grid (where n ≥ 8 is an even number) 

Three kinds of pieces 
- Pichus
- Pikachus
- Raichus

Two different colors 
- Black 
- White

Initially the board starts empty, except for a row of white Pikachus on the second row of the board, a row of white Pichus on the third row of the board, and a row of black Pichus on row n − 2 and a row of black Pikachus on row n − 1

Two players alternate turns, with White going first

In any given turn, a player can choose a single piece of their color and move it according to the rules of that piece.

### Pichu move

	- one square forward diagonally, if that square is empty
	- “jump” over a single Pichu of the opposite color by moving two squares forward diagonally, if that square is empty. The jumped piece is removed from the board as soon as it is jumped.
	
### Pikachu move

	- 1 or 2 squares either forward, left, or right (but not diagonally) to an empty square, as long as all squares in between are also empty.
	- “jump” over a single Pichu/Pikachu of the opposite color by moving 2 or 3 squares forward, left or right (not diagonally), as long as all of the squares between the Pikachu’s start position and jumped piece are empty and all the squares between the jumped piece and the ending position are empty. The jumped piece is removed as soon as it is jumped.
	
### Raichu

	A Raichu is created when a Pichu or Pikachu reaches the opposite side of the board (i.e. when a Black Pichu or Pikachu reaches row 1 or a white Pichu or Pikachu reaches row n). 
	When this happens, the Pichu or Pikachu is removed from the board and subsituted with a Raichu
	
### Raichi move

	- any number of squares forward/backward, left, right or diagonally, to an empty square, as long as all squares in between are also empty.
	- “jump” over a single Pichu/Pikachu/Raichu of the opposite color and landing any number of squares forward/backward, left, right or diagonally, as long as all of the squares between the Raichu’s start position and jumped piece are empty and all the squares between the jumped piece and the ending position are empty. 
		The jumped piece is removed as soon as it is jumped.
	
Note the hierarchy: Pichus can only capture Pichus, Pikachus can capture Pichus or Pikachus, while Raichus can capture any piece. 

The winner is the player who first captures all of the other player’s pieces.

Program accepts a command line argument that gives the current state of the board as a string of .’s, w’s, W’s, b’s, B’s, @’s, and $’s, which indicate which squares have no piece, a white Pichu, a white Pikachu, a black Pichu, a black Pikachu, a white Raichu and a black Raichu respectively, in row-major order. For example, if n = 8, then the encoding of the start state of the game would be:
             
						 ........W.W.W.W..w.w.w.w................b.b.b.b..B.B.B.B........

Program is called with four command line parameters: 

	(1) the value of n
	(2) the current player (w or b)
	(3) the state of the board, encoded as above
	(4) a time limit in seconds
	
Program decides a recommended single move for the given player with the given current board state, and display the new state of the board after making that move






	
	
