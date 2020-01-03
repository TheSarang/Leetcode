# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.flag = True
        
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p == None and q == None:
            return True
        if p == None:
            return False
        if q == None:
            return False
        if (p.val != q.val):
            return False
        self.flag &= self.isSameTree(p.left, q.left)
        self.flag &= self.isSameTree(p.right, q.right)
        return self.flag
