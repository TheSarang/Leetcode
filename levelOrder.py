from queue import Queue

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root == None:
            return []
        
        q1 = Queue()
        q2 = Queue()
        out = []
        out.append([root.val])
        temp = []
        q1.put(root)
        while not q1.empty():
            cur = q1.get()
            for node in self.successor(cur):
                temp.append(node.val)
                q2.put(node)
                
            if q1.empty():
                q1 = q2
                q2 = Queue()
                if temp != []:
                    out.append(temp)
                temp = []
        return out
        
    def successor(self, node):
        return node.children
