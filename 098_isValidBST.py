# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root):
        def helper(node, lower = float('-inf'), upper = float('inf')):
            if node == None:
                return True
            
            if node.val <= lower or node.val >= upper:
                return False
            
            return helper(node.left, lower, node.val) and helper(node.right, node.val, upper)
            
        
        return helper(root)
