# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root, targetSum): 
        def dfs(node, curr, total):

            # break out if null
            if node == None:
                return
            

            nodes = curr.copy()
            nodes.append(node.val)
            total += node.val
            
            # check if leaf and target sum has been reached
            if node.left == None and node.right == None and total == targetSum:
                res.append(nodes)
                
            # get traverse down
            dfs(node.left, nodes, total)
            dfs(node.right, nodes, total)
            
    
        # will modify res variable in place, return that when done
        res = []
        dfs(root, [], 0)
        return res