class Solution:
    def maxSlidingWindow(self, nums, k):
      
      
#       TC = O(Nlogk), worst case O(NlogN) when all elements are in ascending order
#       SC = O(N)
        heap = []
        res = []

        for i, val in enumerate(nums):
            while heap and heap[0][1] <= (i - k):
                heapq.heappop(heap)
            heapq.heappush(heap, (-val ,i))
            if i + 1 >= k:
                res.append(-heap[0][0])
        return res
      
      
      
 #      TC = O(N)
 #      SC = O(N
        res = []
        d = deque()

        for i, v in enumerate(nums):
            #large element on left side to access it
            while d and nums[d[-1]] <= v:
                d.pop()
            d.append(i)

            if d[0] <= i - k:
                d.popleft()
            if i + 1 >= k:
                res.append(nums[d[0]])
        return res
