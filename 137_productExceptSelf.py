class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # Time complexity: O(n)
        # Space complexity: O(n)
    
        output = [1] * len(nums)

        left = 1
        for i in range(len(nums)):
            output[i] *= left
            left *= nums[i]

        right = 1
        for i in range(len(nums)-1, -1, -1):
            output[i] *= right
            right *= nums[i]
         
        return output
