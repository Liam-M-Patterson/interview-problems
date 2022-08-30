class Solution:
    def permuteUnique(self, nums):
        
        letters = {}
        for num in nums:
            if num in letters:
                letters[num] += 1
            else:
                letters[num] = 1
        
        res = []
        
        def backtrack(curr, available):
            if len(available) == 0:
                res.append(curr.copy())
            
            for num in available:
                
                availableCopy = available.copy()
                availableCopy[num] -= 1
                if availableCopy[num] == 0:
                    del availableCopy[num]
                
                curr.append(num)
                backtrack(curr.copy(), availableCopy)
                curr.pop()
                
        backtrack([], letters)
        return res