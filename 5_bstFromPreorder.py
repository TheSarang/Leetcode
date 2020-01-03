# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if preorder == None:
            return []
        root = TreeNode(preorder[0])
        for i in preorder[1:]:
            cur = root
            while cur!=None:
                if i < cur.val:
                    if cur.left == None:
                        cur.left = TreeNode(i)
                        break
                    else:
                        cur = cur.left
                elif i > cur.val:
                    if cur.right == None:
                        cur.right = TreeNode(i)
                        break
                    else:
                        cur = cur.right
        return root
