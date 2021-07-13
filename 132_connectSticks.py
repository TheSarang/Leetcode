import heapq
class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heapq.heapify(sticks)
        res = 0
        while len(sticks) > 1:
            temp = heapq.heappop(sticks) + heapq.heappop(sticks)
            res += temp
            heapq.heappush(sticks, temp)
        return res
