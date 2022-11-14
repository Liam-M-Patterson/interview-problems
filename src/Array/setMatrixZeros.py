# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

# You must do it in place.
# leetcode 73

# Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
# Output: [[1,0,1],[0,0,0],[1,0,1]]

# Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

class Solution:
    def setZeroes(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
    
        # get all unique rows and columns of original zeros.
        zeroRows = []
        zeroCols = []
        for i, row in enumerate(matrix):
            for j, val in enumerate(row):
                if val == 0:
                    if i not in zeroRows:
                        zeroRows.append(i)
                    if j not in zeroCols:
                        zeroCols.append(j)
        
        # set the entire row to zero for each row with a zero
        width = len(matrix[0])
        for row in zeroRows:    
            matrix[row] = [0] * width

        # set column to zero
        height = len(matrix) 
        for col in zeroCols:    
            for row in range(height):
                matrix[row][col] = 0