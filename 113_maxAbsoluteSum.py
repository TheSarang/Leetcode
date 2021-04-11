class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        GM = LMP = LMN = nums[0]
        for i in range(1, len(nums)):
            LMP = max(nums[i]+LMP, nums[i])
            LMN = min(nums[i]+LMN, nums[i])
            GM = max(GM, LMP, -LMN)
        return abs(GM)
            
