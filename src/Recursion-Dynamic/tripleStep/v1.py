import sys

class Solution:

    def __init__(self, steps: int):

        memo = [-1]*(steps+1)

        self.num = self.countWays(steps, memo)
    
    def countWays(self, steps, memo):
        
        if steps < 0:
            return 0
        elif steps == 0:
            return 1
        elif memo[steps] > - 1:
            return memo[steps]
        else:
            memo[steps] = self.countWays(steps -1, memo) + self.countWays(steps-2, memo) + self.countWays(steps-3, memo)
            return memo[steps]



if __name__ == "__main__":
    
    res = Solution(int(sys.argv[1]))
    print(res.num)