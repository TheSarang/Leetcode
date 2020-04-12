class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones)>1:
            stones.sort()
            m1=stones.pop()
            m2=stones.pop()
            if m1 != m2:
                stones.append(abs(m1-m2))      
        if stones:
            return stones[0]
        else:
            return 0
            
#------------------------------------

from heapq import heappush, heappop
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for stone in stones:
            heappush(heap, -1*stone)
        while len(heap) > 1:
            first, second = heappop(heap), heappop(heap)
            print(first)
            print(second)
            heappush(heap, first - second)
        return (-1*heap[-1])
