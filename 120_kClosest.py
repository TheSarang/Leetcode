class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        # TC = O(N*logk)
        for (x, y) in points:
            dist = -(math.pow((0-x),2) + math.pow((0-y),2))
            if len(heap) == k:
                heapq.heappushpop(heap, (dist, x, y))
            else:
                heapq.heappush(heap, (dist, x, y))
        
        return [(x,y) for (dist, x, y) in heap]
