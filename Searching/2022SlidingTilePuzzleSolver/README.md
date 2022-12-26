# The 2022 Puzzle

The 2022 puzzle, is a lot like the 9-puzzle

    1. It has 25 tiles, so there are no empty spots on the board; 
    2. instead of moving a single tile into an open space, a move in this puzzle consists of either 
        a. Sliding an entire row of tiles left or right one space, with the left- or right-most tile ‘wrapping around’ to the other side of the board
        b. Sliding an entire column of tiles up or down one space, with the top- or bottom-most tile ‘wrapping around’ to the other side of the board
        c. Rotating the outer ‘ring’ of tiles either clockwise or counterclockwise
        d. Rotating the inner ring either clockwise or counterclockwise
        
### Goal:
    Find a short sequence of moves that restores the canonical configuration given an initial board configuration
    
#### The moves are encoded as strings in the following way:
    • For sliding rows, R (right) or L (left), followed by the row number indicating the row to move left or right. The row numbers range from 1-5.
    • For sliding columns, U (up) or D (down), followed by the column number indicating the column to move up or down. The column numbers range from 1-5.
    • For rotations, I (inner) or O (outer), followed by whether the rotation is clockwise (c) or counterclock- wise (cc).
