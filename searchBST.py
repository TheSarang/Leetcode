# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root == None:
            return 
        elif root.val == val:
            return root
        elif root.val < val:
            node = self.searchBST(root.right, val)
        elif root.val > val:
            node = self.searchBST(root.left, val)
        return node
