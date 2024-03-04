# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Recursive

class Solution:
    def __init__(self):
        self.list1 = []
        
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root == None:
            return
        self.inorderTraversal(root.left)
        self.list1.append(root.val)
        self.inorderTraversal(root.right)
        return self.list1

# Iterative

class Solution:
    def __init__(self):
        self.list1 = []
        
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
        ans = []
        cur = root
        while True:
          if cur != None: 
            stack.append(cur)
            cur = cur.left
          elif stack:
            cur = stack.pop()
            ans.append(cur.val)
            cur = cur.right
          else:
            break
        return ans
                
                
