# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.sum = 0
        
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        def find(root, val='root'):
            if root == None:
                return
            find(root.left, 'left')
            if (root.left == None and root.right == None) and val == 'left':
                self.sum +=root.val
            find(root.right, 'right')
        find(root)
        return self.sum
        
