# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.flag = False
        
    def _helper(self, s, t):
        if s == None and t == None:
            return True
        elif s != None and t != None and s.val == t.val:
            return self._helper(s.left, t.left) & self._helper(s.right, t.right)
        else:
            return False
            
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if s == None:
            return False
        if s != None:
            if s.val == t.val:
                self.flag |= self._helper(s, t)
        self.isSubtree(s.left, t)
        self.isSubtree(s.right, t)
        return self.flag
