class Solution:
    def trap(self, height: List[int]) -> int:
        if height == []:
            return 0
        left_array = [0 for _ in range(len(height))]
        right_array = [0 for _ in range(len(height))]
        
        left_array[0] = height[0]
        
        for i in range(1, len(height)):
            left_array[i] = max(height[i], left_array[i-1])
                              
        right_array[-1] = height[-1]
        
        for i in range(len(height)-2, -1, -1):
            right_array[i] = max(height[i], right_array[i+1])
        
        count = 0 
        for i in range(len(height)):
            count += min(left_array[i], right_array[i]) - height[i]
        return(count)
