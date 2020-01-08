class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        sum1 = 0
        result = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                sum1 += 1
            else:
                if sum1 > result:
                    result = sum1
                sum1 = 0
        if sum1 > result:
            result = sum1
        return result
