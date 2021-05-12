from collections import defaultdict
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_ = defaultdict(int)
        for num in nums:
            dict_[num] += 1
        # return heapq.nlargest(k, dict_.keys(), key = dict_.get)
        return [pair[0] for pair in heapq.nlargest(k, dict_.items(), key = lambda x:x[1])]
        
