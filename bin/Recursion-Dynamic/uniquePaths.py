class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        paths = {}
    
        def numFromPos(row, col):
            
            if (row == m -1 or col == n -1):
                return 1

            res = 0

            if ((row + 1, col) in paths):
                res += paths[(row+1, col)]
            else:
                numPaths = numFromPos(row+1, col)
                res += numPaths
                paths[(row+1, col)] = numPaths

            if ((row, col+1) in paths):
                res += paths[(row, col+1)]
            else:
                numPaths = numFromPos(row, col+1)
                res += numPaths
                paths[(row, col+1)] = numPaths

            
            return res
        
        return numFromPos(0,0)

if __name__ == "__main__":
    
    sol = Solution()

    print(sol.uniquePaths(3, 7))