"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

from queue import Queue

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root == None:
            return 0
        q1 = Queue()
        q2 = Queue()
        q1.put(root)
        count=0
        while not q1.empty():
            curr = q1.get()
            for i in self.successor(curr):
                q2.put(i) 
            if q1.empty():
                q1 = q2
                q2 = Queue()
                count+=1
        return count
    
    def successor(self,node):
        return node.children
        
