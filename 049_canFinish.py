from queue import Queue
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = dict()
        inDegree = dict()
        visited = []
        q = Queue()
        for nodes in prerequisites:
            if not nodes[1] in adjList:
                adjList[nodes[1]] = [nodes[0]]
            else:
                adjList[nodes[1]].append(nodes[0])
                
            if not nodes[0] in inDegree:
                inDegree[nodes[0]] = 1
            else:
                inDegree[nodes[0]] += 1
        
        for i in range(numCourses):
            if not i in inDegree:
                q.put(i)
        
        while not q.empty():
            cur = q.get()
            if cur in adjList:
                for nodes in adjList[cur]:
                    if nodes in inDegree:
                        temp = inDegree[nodes]
                        temp -= 1
                        inDegree[nodes] = temp
                        if inDegree[nodes] == 0:
                            q.put(nodes)
            visited.append(cur)
        
        return numCourses == len(visited)
                    
                    
        
                
