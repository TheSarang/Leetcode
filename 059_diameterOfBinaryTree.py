# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.maxVal = 0
        
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def _helper(root):
            if root == None:
                return 0
            left = _helper(root.left)
            right = _helper(root.right)
            self.maxVal = max(self.maxVal, left + right)
            return max(left, right) + 1
        
        _helper(root)
        return self.maxVal
