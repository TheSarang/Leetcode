class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict1 = {}
        for i in range(len(nums)):
            if nums[i] in dict1.keys():
                return [dict1[nums[i]], i]
            else:
                dict1[target - nums[i]] = i
