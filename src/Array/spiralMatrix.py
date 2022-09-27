
from enum import Enum
# Make a custome Direction class to handle direction of travel slightly easier
class Direction(Enum):
    RIGHT = 1
    DOWN = 2
    LEFT = 3
    UP   = 4

    
class Solution:
    def spiralOrder(self, matrix) :
        
        # set initial direction to right, since we go clockwise
        direction = Direction.RIGHT
        visited = [ [False for i in matrix[0]] for j in matrix]
        
        COLS = len(matrix[0])
        ROWS = len(matrix)
        
        res = []
        row, col = 0, 0
        
        while row < ROWS and row >= 0 and col < COLS and COLS >= 0 and visited[row][col] == False:

            # add current number to the output, and update visited array
            res.append(matrix[row][col])
            visited[row][col] = True

            if direction == Direction.RIGHT:
                
                # if there is still space in this direction, continue
                if col + 1 < COLS and not visited[row][col+1]:
                    col += 1
                else:
                    # change direction
                    row += 1
                    direction = Direction.DOWN

            elif direction == Direction.DOWN:
                
                if row + 1 < ROWS and not visited[row+1][col]:
                    row += 1
                else:
                    col -= 1
                    direction = Direction.LEFT

            elif direction == Direction.LEFT:
                
                if col - 1 >= 0 and not visited[row][col-1]:
                    col -= 1
                else:
                    row -= 1
                    direction = Direction.UP
            else: # UP
                
                if row - 1 >= 0 and not visited[row-1][col]:
                    row -= 1
                else:
                    col += 1
                    direction = Direction.RIGHT
        return res
            