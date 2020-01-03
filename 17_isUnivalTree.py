# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        stack = []
        cur = root
        ans = []
        while True:
            if cur is not None:
                stack.append(cur)
                cur = cur.left
            elif stack:
                cur = stack.pop()
                if cur.val != root.val:
                    return False
                cur = cur.right
            else:
                break
        return True
