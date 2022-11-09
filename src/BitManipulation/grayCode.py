# Problem Description
# An n-bit gray code sequence is a sequence of 2n integers where:

# Every integer is in the inclusive range [0, 2n - 1],
# The first integer is 0,
# An integer appears no more than once in the sequence,
# The binary representation of every pair of adjacent integers differs by exactly one bit, and
# The binary representation of the first and last integers differs by exactly one bit.
# Given an integer n, return any valid n-bit gray code sequence.

# Input: n = 2
# Output: [0,1,3,2]
# Explanation:
# The binary representation of [0,1,3,2] is [00,01,11,10].
# - 00 and 01 differ by one bit
# - 01 and 11 differ by one bit
# - 11 and 10 differ by one bit
# - 10 and 00 differ by one bit
# [0,2,3,1] is also a valid gray code sequence, whose binary representation is [00,10,11,01].
# - 00 and 10 differ by one bit
# - 10 and 11 differ by one bit
# - 11 and 01 differ by one bit
# - 01 and 00 differ by one bit

class Solution:
    def grayCode(self, n: int):

        # always start with 0
        res = [0]

        # generate all nums available to be chose
        numsAvailable = {i for i in range(1,2**n)}

        # numbers remain to be chosen
        while len(numsAvailable):
            
            # flip the first bit
            num = res[-1] ^ 1
            i = 1

            # num not available
            while num not in numsAvailable:
                # flip the ith bit
                num = res[-1] ^ (1 << i) 
                i += 1

            # add num to the solution
            res.append(num)
            # remove num from being selected again
            numsAvailable.remove(num)
            
        return res


# used to verify the results
def bitsDiff(x, y):
    numDiff = 0

    while x or y and numDiff < 2:
        numDiff += 1 if (x&1) != (y&1) else 0
        x >>= 1
        y >>= 1

    return numDiff

def testGrayCode(grayCode):
    try:
        for i in range(len(grayCode)-1):
        
            if bitsDiff(grayCode[i], grayCode[i+1]) != 1:
                raise Exception('Error: answer is not valid gray code')

        if bitsDiff(grayCode[0], grayCode[-1]) != 1:
                raise Exception('Error: answer is not valid gray code')
        print('Valid gray code')

    except Exception as e:
        print(str(e))



solution = Solution()
grayCode = solution.grayCode(3)
testGrayCode(solution.grayCode(3))
testGrayCode(solution.grayCode(10))
testGrayCode([i for i in range(2**5)])