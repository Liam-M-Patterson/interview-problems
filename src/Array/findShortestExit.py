# Leetcode 1926
# Tags: Breadth First Search, Array
# You are given an m x n matrix maze (0-indexed) with empty cells (represented as '.') and walls (represented as '+'). You are also given the entrance of the maze, where entrance = [entrancerow, entrancecol] denotes the row and column of the cell you are initially standing at.

# In one step, you can move one cell up, down, left, or right. You cannot step into a cell with a wall, and you cannot step outside the maze. Your goal is to find the nearest exit from the entrance. An exit is defined as an empty cell that is at the border of the maze. The entrance does not count as an exit.

# Return the number of steps in the shortest path from the entrance to the nearest exit, or -1 if no such path exists.

# Example 1:
# Input: maze = [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]], entrance = [1,2]
# Output: 1
# Explanation: There are 3 exits in this maze at [1,0], [0,2], and [2,3].
# Initially, you are at the entrance cell [1,2].
# - You can reach [1,0] by moving 2 steps left.
# - You can reach [0,2] by moving 1 step up.
# It is impossible to reach [2,3] from the entrance.
# Thus, the nearest exit is [0,2], which is 1 step away.

# Example 2:
# Input: maze = [["+","+","+"],[".",".","."],["+","+","+"]], entrance = [1,0]
# Output: 2
# Explanation: There is 1 exit in this maze at [1,2].
# [1,0] does not count as an exit since it is the entrance cell.
# Initially, you are at the entrance cell [1,0].
# - You can reach [1,2] by moving 2 steps right.
# Thus, the nearest exit is [1,2], which is 2 steps away.

# Example 3:
# Input: maze = [[".","+"]], entrance = [0,0]
# Output: -1
# Explanation: There are no exits in this maze.

from collections import deque 
class Solution:
    # do breadth first appoach. as soon as exit is found, return the number of steps 
    def nearestExit(self, maze, entrance):
        height = len(maze)
        width = len(maze[0])
        row, col = entrance
        
        def isExit(x, y):
            if x == 0 or y == 0:
                return True
            if x == height-1 or y == width-1:
                return True
            return False

        def adjacent(i, j, dirs=[1, 0, -1, 0, 1]):
            for d in range(4):
                x = i + dirs[d]
                y = j + dirs[d+1]
                if 0 <= x < height and 0 <= y < width and maze[x][y] != '+':
                    yield x, y
        
        queue = deque([(row, col, 0)])
        maze[row][col] = '+'
        while queue: #there are still cells to visit
            x, y, steps = queue.popleft() #get first cell added     
            
            for row, col in adjacent(x, y): # loop through all the adjacent cells that haven't been visited
                maze[row][col] = '+' #mark as visited
                if isExit(row, col): #if it is an exit, return
                    return steps + 1 
                queue.append((row, col, steps+1)) #not an exit, add it to the queue
        return -1  #no exit found
                
        
    # # MY own DFS solution, solves 189/194 test cases, gets incorrect output on the test
    # def nearestExit(self, maze, entrance) -> int:
    #     print(maze)
    #     height = len(maze)
    #     width = len(maze[0]) 

    #     dp = {}
    #     maze[entrance[0]][entrance[1]] = 'X'
    #     # return number of steps from positon
    #     def dfs(row, col):

    #         if row >= height or row < 0 or col >= width or col < 0:
    #             return -1

    #         if (row, col) in dp:
    #             return dp[(row, col)]

    #         if maze[row][col] != '.':
    #             dp[(row, col)] = float("inf")
    #             return float("inf")

            
    #         maze[row][col] = 'x'

    #         dp[(row, col)] = min(dfs(row-1, col), dfs(row+1, col), dfs(row, col-1), dfs(row, col+1)) + 1
    #         return dp[(row, col)]
        
    #     def getDP(row, col):
    #         if (row, col) in dp:
    #             return dp[(row, col)]
    #         return float("inf")

    #     row = entrance[0]
    #     col = entrance[1]

    #     if row + 1 < height and maze[row+1][col] == '.':
    #         print('down')
    #         dfs(row+1, col)

    #     if row - 1 < height and maze[row-1][col] == '.':
    #         print('up')
    #         dfs(row-1, col)

    #     if col+1 < width and maze[row][col+1] == '.':
    #         print('right')
    #         dfs(row, col+1)
        
    #     if col-1 < width and maze[row][col-1] == '.':
    #         print('left')
    #         dfs(row, col-1)
    #     # dfs(row, col)
    #     print(dp)
        
    #     shortest = min(getDP(row+1, col), getDP(row-1, col), getDP(row, col+1), getDP(row, col-1)) 
    #     return shortest + 1 if shortest != float('inf') else -1
    #     # return dp[(entrance[0], entrance[1])]

            