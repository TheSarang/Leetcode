import math
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        '''
        BF
        
        1] sort an array based on distance return k values
        '''
        
        # points.sort(key=lambda x: (x[0]+x[0])**2 + (x[1]+x[1])**2)
        # return points[:k]
    
    
        '''
        heaps
        1] create max heap
        2] put elemtns k time 
        3] pop from heap if len(heap) > k then push new value and then pop it
        
        '''
        heap = []
        for pair in points:
            x = pair[0]
            y = pair[1]
            distance = x*x + y*y
            heapq.heappush(heap, (-distance, (x,y)))
            if len(heap) > k:
                heapq.heappop(heap)
        return (pair[1] for pair in heap)
                
