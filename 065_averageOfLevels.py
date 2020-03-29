# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from queue import Queue
import math
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if root == None:
            return None
        queue1 = Queue()
        queue2 = Queue()
        temp = []
        result = [root.val]
        queue1.put(root)
        while not queue1.empty():
            cur = queue1.get()
            for nodes in self._helper(cur):
                if nodes == None:
                    continue
                temp.append(nodes.val)
                queue2.put(nodes)
            
            if queue1.empty():
                queue1 = queue2
                if len(temp) != 0:
                    result.append(sum(temp)/len(temp))
                queue2 = Queue()
                temp = []
        return result
    
    def _helper(self, node):
        return [node.left, node.right]
