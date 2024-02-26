class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        # TC = O(N*logk)
        # SC = O(K)
        for (x, y) in points:
            dist = -(math.pow((0-x),2) + math.pow((0-y),2))
            if len(heap) == k:
                heapq.heappushpop(heap, (dist, x, y))
            else:
                heapq.heappush(heap, (dist, x, y))
        
        return [(x,y) for (dist, x, y) in heap]
  
#-----------------------------------------------------------------------------------------------------------------------------------------------------

import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        # TC = O(NlogN) + O(KlogN)
        # SC = O(N)
        for x,y in points:
            distance = math.sqrt((0-x)**2 + (0-y)**2)
            heapq.heappush(heap, (distance, (x,y)))
        return [pair[1] for pair in heapq.nsmallest(k, heap, key= lambda x:x[0])]
        
#-----------------------------------------------------------------------------------------------------------------------------------------------------
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:    
        dict_ = {}
        res = []
        # TC = O(N)+ O(NlogN) + O(K)
        # SC = O(N)
        for x,y in points:
            distance = math.sqrt((0-x)**2 + (0-y)**2)
            dict_[(x,y)] = distance
        
        dict_sorted = sorted(dict_.items(), key = lambda kv:(kv[1])) 
        for i in range(k):
            res.append(dict_sorted[i][0])
        
        return res
