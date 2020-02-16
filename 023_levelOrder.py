# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from queue import Queue
class Solution:
    def __init__(self):
        self.list = []
    
    def check(self, root, level):  
        if root == None:
            return
        if level == len(self.list):
            self.list.append([root.val])
        elif level < len(self.list):
            self.list[level].append(root.val)
            
        self.check(root.left, level+1)
        self.check(root.right, level+1)
            
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return []
        self.check(root, 0)
        return self.list
    
 # ------------------------------------------------------------------------------      
   
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return None
        q1 = Queue()
        q2 = Queue()
        q1.put(root)
        list1 = [[root.val]]
        temp = []
        while not q1.empty():
            cur = q1.get()
            for nodes in self._helper(cur):
                if nodes == None:
                    continue
                temp.append(nodes.val)
                q2.put(nodes)
                
            if q1.empty():
                q1 = q2
                if temp != []:
                    list1.append(temp)
                q2 = Queue()
                temp = []
        
        return list1
    
    def _helper(self, node):
        return [node.left, node.right]
