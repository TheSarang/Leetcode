import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        
        while k < len(nums):
            heapq.heappop(nums)
        return nums[0]
