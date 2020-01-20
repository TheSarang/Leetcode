# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.sum = 0
        self.maxLevel = -1
        
    def dfs(self, root, level):
        if root == None:
            return
        if self.maxLevel < level:
            self.maxLevel = level
            self.sum = root.val
        elif (self.maxLevel == level):
            self.sum += root.val
        self.dfs(root.left, level+1)
        self.dfs(root.right, level+1)
            
    def deepestLeavesSum(self, root: TreeNode) -> int:
        self.dfs(root, 0)     
        return self.sum
