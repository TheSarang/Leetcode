class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        adjList = dict()
        inDegree = dict()
        for pair in trust:
            if pair[1] not in inDegree:
                inDegree[pair[1]] = 1
            else:
                inDegree[pair[1]] += 1
            if pair[0] not in adjList:
                adjList[pair[0]] = [pair[1]]
            else:
                adjList[pair[0]].append(pair[1])
        print(adjList)
        print(inDegree)
        temp = 0
        for i in range(1, N+1):
            if (i not in adjList):
                temp = i
        for key, vals in adjList.items():
            if temp not in vals:
                return -1
        return temp
        
