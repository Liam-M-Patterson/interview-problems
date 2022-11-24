# Leetcode 79 Tags: Array, Matrix, Backtracking
# Given an m x n grid of characters board and a string word, return true if word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

# Example 1:
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
# Output: true

# Example 2:
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
# Output: true

# Example 3:
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
# Output: false
class Solution:
    def exist(self, board, word: str) -> bool:
        
        ROWS = len(board)
        COLS = len(board[0])

        def dfs(x, y, visited, i=0):
            if i >= len(word):
                return True

            if x < 0 or y < 0 or x >= ROWS or y >= COLS:
                return False

            if (x,y) in visited:
                return False
            
            if board[x][y] == word[i]:
                
                visited.add((x,y))
                i +=1
                a = dfs(x+1, y, visited, i)
                b = dfs(x-1, y, visited, i)
                c = dfs(x, y+1, visited, i)
                d = dfs(x, y-1, visited, i)
                visited.remove((x,y))
                return a or b or c or d

        
        for x in range(ROWS):
            for y in range(COLS):
                if dfs(x, y, set()):
                    return True

        return False