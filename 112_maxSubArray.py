class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        # Kadane's Algo
        # TC: O(n)
        # SC: O(1)
        
        LM = GM = nums[0]
        for i in range(1, len(nums)):
            LM = max(nums[i], nums[i] + LM)
            GM = max(GM, LM)
            
        return GM
