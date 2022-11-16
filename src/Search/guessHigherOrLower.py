# We are playing the Guess Game. The game is as follows:

# I pick a number from 1 to n. You have to guess which number I picked.

# Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

# You call a pre-defined API int guess(int num), which returns three possible results:

# -1: Your guess is higher than the number I picked (i.e. num > pick).
# 1: Your guess is lower than the number I picked (i.e. num < pick).
# 0: your guess is equal to the number I picked (i.e. num == pick).
# Return the number that I picked.

# mimic the api provided by leetcode
def guess(num):
    if num > answer:
        return -1
    elif num < answer:
        return 1
    else:
        return 0
    
class Solution:
    def guessNumber(self, n):

        l, r = 1, n
        while True:
            num = (l+r)//2
            guessRes = guess(num)
            if guessRes == -1:
                r = num-1
            elif guessRes == 1:
                l = num+1
            else:
                return num

sol = Solution()

answer = 10
print(sol.guessNumber(200))

answer = 1314
print(sol.guessNumber(3400))

answer = 919
print(sol.guessNumber(1000))