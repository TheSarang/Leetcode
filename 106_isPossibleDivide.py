from collections import Counter

class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        dict_ = Counter(nums)
        nums.sort()
        print(dict_)
        i, n = 0, len(nums)
        while i < n:
            curr = nums[i]
            for j in range(k):
                now = curr+j
                if now not in dict_:
                    return False
                dict_[now] -= 1
                if dict_[now] == 0:
                    del dict_[now]
            while i < n and nums[i] not in dict_:
                i+=1
        return True
        
