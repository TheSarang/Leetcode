# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from queue import Queue
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if root == None:
            return None
        self.result = [root.val]
        temp = []
        q1 = Queue()
        q2 = Queue()
        q1.put(root)
        while not q1.empty():
            cur = q1.get()
            for nodes in self._helper(cur):
                if nodes == None:
                    continue
                temp.append(nodes.val)
                q2.put(nodes)
            
            if q1.empty():
                q1 = q2
                q2 = Queue()
                if temp != []:
                    self.result.append(temp[-1])
                temp = []
        return self.result
                
                
    def _helper(self, node):
        return [node.left, node.right]
