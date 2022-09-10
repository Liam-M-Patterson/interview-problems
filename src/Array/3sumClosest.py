class Solution:
    def threeSumClosest(self, nums, target):
        
        nums.sort()
        closest = nums[0] + nums[-1] + nums[len(nums)//2]
        
        for i in range(len(nums)):
            
            l = i + 1
            r = len(nums) - 1
            
            while l < r:
                
                total = nums[i] + nums[l] + nums[r]
                     
                 #decreasing difference between current closest and target
                if abs(target - total) <= abs(target - closest):        
                    closest = total
        
                if total > target:
                
                    r -= 1
                elif total < target:
                
                    l += 1
                else:
                
                    return total

        return closest