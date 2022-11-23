# Leetcode 36. Tags: Array, Matrix 
# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note:

# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.

# Example 1:
# Input: board = 
# [["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: true

# Example 2:
# Input: board = 
# [["8","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: false
# Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.

class Solution:
    def isValidSudoku(self, board) -> bool:

        def isUnique(ch, unique):
            if ch != '.':
                if ch not in unique:
                    unique.add(ch)
                else:
                    return False
            return True

        def checkRow(i):
            unique = set()
            for ch in board[i]:
                if not isUnique(ch, unique):
                    return False
            return True
            
        def checkCol(i):
            unique = set()
            for row in board:
                ch = row[i]
                if not isUnique(ch, unique):
                    return False
            return True
            
        def checkBox(i):
            
            baseRow = (i // 3) * 3 #have 3 "big baseRows"
            baseCol = (i % 3) * 3 # have 3 "big baseCols"
            unique = set()
            
            for x in range(baseRow, baseRow+3):
                for y in range(baseCol, baseCol+3):
                    ch = board[x][y]
                    if not isUnique(ch, unique):
                        return False
            return True

        # Main body of code
        isValid = True
        i = 0
        # loop thorough the size of the board, checking a row, column and 3x3 grid each time
        while isValid and i < 9:
            isValid = checkRow(i)
            isValid = isValid and checkCol(i)
            isValid = isValid and checkBox(i)
            i += 1
        
        return isValid
        

board1 =[["5","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]

board2 =[["8","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]


def verify(correct):
    if correct:
        print("pass")
    else:
        print("failed")
        
validator = Solution()
verify(validator.isValidSudoku(board1) == True) 
verify(validator.isValidSudoku(board2) == False) 