class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # kadane algo
        GM = LMP = LMN = nums[0]
        for i in range(1, len(nums)):
            x = max(nums[i], nums[i]*LMN, nums[i]*LMP)
            y = min(nums[i], nums[i]*LMN, nums[i]*LMP)
            LMP, LMN = x, y
            GM = max(LMP, GM)
        return GM
