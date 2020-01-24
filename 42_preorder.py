"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    def __init__(self):
        self.list1 = []
        self.flag = True
        
    def preorder(self, root: 'Node') -> List[int]:
        if root == None:
            return []
        elif root.children == None:
            return [root.val]
        elif root.children != None:
            for node in root.children:
                if self.flag:
                    self.list1.append(root.val)
                    self.flag = False
                self.list1.append(node.val)
                self.preorder(node)
            return self.list1
     # -------------------------------------------------------   
        if not root:
            return []      
        result = [root.val]
        if root.children is not None:
            for child in root.children:
                result.extend(self.preorder(child))
            return result
            
        
