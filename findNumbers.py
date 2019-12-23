class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        dict1  = {}
        count = 0
        for i in nums:
            if i not in dict1:
                dict1[i] = str(i)
        for i in nums:
            if len(dict1[i]) % 2 == 0:
                count+=1
                
        return count
