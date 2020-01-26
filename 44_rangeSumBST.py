# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.num = 0
        
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        
        if root == None:
            return
        self.rangeSumBST(root.left, L, R)
        if (root.val >= L) and (root.val <= R):
            self.num+=root.val
        self.rangeSumBST(root.right, L, R)
        return self.num
        
