class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # Time complexity: O(n)
        # Space complexity: O(n)
    
        n = len(nums)
        result = [0]*n
        
        prefix_product = 1
        for i in range(n):
            result[i] = prefix_product
            prefix_product *= nums[i]

        postfix_product = 1
        for i in range(n-1,-1,-1):
            result[i] *= postfix_product
            postfix_product *= nums[i]
            
        return result
