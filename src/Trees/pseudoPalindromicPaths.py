# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths(self, root):
        
        answer = 0
        def dfs(root, path):
            
            if root == None:
                return
            
            curr = path.copy() 
            #keep track of parity in a hashamp
            if root.val in curr:
                # if already occurred, remove
                del curr[root.val]
            else:
                # add new occurrance
                curr[root.val] = 1
            
            
            
            if root.left == None and root.right == None:
                # if there is one pivot point, or none, then it is palindrome
                if len(curr) <= 1:
                    nonlocal answer
                    answer += 1

            dfs(root.left, path)
            dfs(root.right, path)
            
        
        dfs(root, {})
        return answer
    
