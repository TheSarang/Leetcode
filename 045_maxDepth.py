# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.maxL = -1
    def calc(self, root, level):
        if root == None:
            return self.maxL
        if level > self.maxL:
            self.maxL = level
        self.calc(root.left, level+1)
        self.calc(root.right, level+1)

    def maxDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        self.calc(root, 1)
        return self.maxL
