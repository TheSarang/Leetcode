class Solution:
    def maxArea(self, height: List[int]) -> int:
        # BRUTE FORCE
        # TIME COMPLEXITY: O(N^2)
        # SPACE COMPLEXITY: O(N^2)
        res = 0
        for i in range(len(ht)):
            for j in range(i+1, len(ht)):
                length = j - i
                min_height = min(ht[i], ht[j])
                area = length * min_height
                res = max(res, area)
        return res


        # OPTIMIZED FORCE
        # TIME COMPLEXITY: O(N)
        # SPACE COMPLEXITY: O(N)
        res = 0
        l, r = 0, len(ht) - 1

        while l < r:
            min_height = min(ht[l], ht[r])
            area = (r - l) * min_height
            res = max(res, area)
            if ht[l] < ht[r]:
                l+=1
            else:
                r-=1
        
        return res
