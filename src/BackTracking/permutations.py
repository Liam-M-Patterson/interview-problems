class Solution:
    def permute(self, nums):
        
        res = []        
    
        def makePerm(available, curr):
            
            if len(available) == 0:
                res.append(curr.copy())
                return
            
            for num in available:
                curr.append(num)
                newAvail = available.copy()
                del newAvail[num]
                makePerm(newAvail, curr)
                curr.pop()
            
        
        hashMap = dict.fromkeys(nums, True)
        
        makePerm(hashMap, [])
        return res
