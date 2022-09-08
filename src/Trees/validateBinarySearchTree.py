# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root) :
       
        def dfs(root, l, r):
            
            # empty tree is valid
            if root == None: return True
            
            # check if current value is within proper range
            if not (root.val < r and root.val > l): return False
            
            # update the bounds of the l and r value, based on direction travelled
            return dfs(root.left, l, root.val) and dfs(root.right, root.val, r)

        # first node has no bounds, give it inf to start
        return dfs(root, float('-inf'), float('inf'))