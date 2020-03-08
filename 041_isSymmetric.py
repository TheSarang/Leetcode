# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def check(self, root1, root2):
        if root1 == None and root2 == None:
            return True
        elif root1 != None and root2 != None and root1.val == root2.val:
            return self.check(root1.left, root2.right) & self.check(root1.right, root2.left)
        else:
            return False
        
    def isSymmetric(self, root: TreeNode) -> bool:
        if root == None:
            return True
        return self.check(root.left, root.right)
        
#------------------------------------------------------------------------------------                     
           
    def __init__(self):
        self.arr1 = []
        self.arr2 = []
            
    def isSymmetric(self, root: TreeNode) -> bool:
        if root == None:
            return True
        def preOrder(root):
            if root == None:
                self.arr1.append(None) 
                return 
            self.arr1.append(root.val)
            preOrder(root.left)
            preOrder(root.right)
            
        def postOrder(root):
            if root == None:
                self.arr2.append(None) 
                return
            self.arr2.append(root.val)
            postOrder(root.right)
            postOrder(root.left)
        
        preOrder(root.left)
        postOrder(root.right)
        print(self.arr1)
        print(self.arr2)
        if self.arr1 == self.arr2:
            return True
        else:
            return False
            
