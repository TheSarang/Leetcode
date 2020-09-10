# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root == None:
            return False
        if root.left == None and root.right == None and root.val == sum:
            return True
        
        sum-=root.val
        left = self.hasPathSum(root.left, sum)
        right = self.hasPathSum(root.right, sum)
        return right or left
