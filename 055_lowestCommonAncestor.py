# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.ancestor = None
        
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def _helper(root, low, high):
            if root == None:
                return None
            if low <= root.val <= high:
                self.ancestor = root
                return 
            elif high > root.val:
                right = _helper(root.right, low, high)
            elif low < root.val:
                left = _helper(root.left, low, high)
                 
        high = low = 0
        if p.val > q.val:
            high = p.val
            low = q.val
        else:
            high = q.val
            low = p.val
        
        _helper(root, low, high)
        return self.ancestor
            
