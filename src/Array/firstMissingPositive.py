# Leetcode 41 First Missing Positive
# Given an unsorted integer array nums, return the smallest missing positive integer.

# You must implement an algorithm that runs in O(n) time and uses constant extra space.

 

# Example 1:
# Input: nums = [1,2,0]
# Output: 3
# Explanation: The numbers in the range [1,2] are all in the array.

# Example 2:
# Input: nums = [3,4,-1,1]
# Output: 2
# Explanation: 1 is in the array but 2 is missing.

# Example 3:
# Input: nums = [7,8,9,11,12]
# Output: 1
# Explanation: The smallest positive integer 1 is missing.
 

# Constraints:
# 1 <= nums.length <= 105
# -231 <= nums[i] <= 231 - 1
class Solution:
    def firstMissingPositive(self, nums):
        
        # mark all negatives as 0, since they do not affect the solution
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0
        
        # make the values occuring in the array have their index be negative to indicate they exist
        for j in range(len(nums)):
            # take the absolute value, since it could have been marked as negative from a previous number
            J = abs(nums[j])

            # check if it is in the bounds of the array
            if 1 <= J <= len(nums):
                # mark the index of the number j as negative, indicating j is in the array
                if nums[J-1] > 0:
                    nums[J-1] *= -1 
                    
                # if the number at index for j is 0, make it the worst case solution
                elif nums[J-1] == 0:
                    nums[J-1] = -(len(nums)+1)

        for i in range(1,len(nums)+1):

            if nums[i-1] >= 0:
                return i
        return len(nums)+1


if __name__ == '__main__':
    sol = Solution()
    
    print(3 == sol.firstMissingPositive([1,2,0]))
    print(2 == sol.firstMissingPositive([3,4,-1,1]))
    print(1 == sol.firstMissingPositive([7,8,9,11,12]))