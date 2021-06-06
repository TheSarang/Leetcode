from collections import defaultdict
import heapq
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        dict_ = defaultdict(int)
        for word in words:
            dict_[word] += 1
        return [pair[0] for pair in heapq.nsmallest(k, dict_.items(), key= lambda item: (-item[1], item[0]))]        
