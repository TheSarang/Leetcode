# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        self.tempStr = ""
        array = []
        def _helper(root):
            if root == None:
                return None
            if root.left == None and root.right == None:
                array.append(self.tempStr + str(root.val))
                return self.tempStr
            if root.left != None:
                self.tempStr += str(root.val)
            elif root.right != None:
                self.tempStr += str(root.val)
            
            left = _helper(root.left)
            right = _helper(root.right)
            self.tempStr = self.tempStr[:-1]
            return self.tempStr
        
        _helper(root)
        totSum = 0
        for num in array:
            totSum += int(num)
        return totSum
            
