# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root):
        
        answer = 0
        def dfs(root, path):
            
            if root == None:
                return
            
            #store even/odd parity in bit position
            #XOR will zero a 1 bit and set a 0 bit to 1
            path = path ^ (1 << root.val)
            
            if root.left == None and root.right == None: #if leaf node
                
                if path & (path - 1) == 0: #check if path is a power of 2 (only one bit set) or 0. 
                    nonlocal answer
                    answer += 1

            dfs(root.left, path)
            dfs(root.right, path)
            
        dfs(root, 0)
        return answer