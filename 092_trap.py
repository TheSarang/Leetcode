class Solution:
    def trap(self, height: List[int]) -> int:
        
        # space complexity -> O(1)
        # time complexity -> O(3n)
        max_h_idx = 0
        max_h = 0
        res = 0
        for i in range(len(height)):
            if height[i] > max_h:
                max_h = max(height[i], max_h)
                max_h_idx = i
                
        max_h_left = 0
        for i in range(max_h_idx):
            max_h_left = max(max_h_left, height[i])
            res += max_h_left - height[i]
        
        max_h_right = 0
        for i in range(len(height)-1, max_h_idx, -1):
            max_h_right = max(max_h_right, height[i])
            res += max_h_right - height[i]
            
        return res
    
#     -----------------------------------------------------------------
        
        # space complexity -> O(2n)
        # time complexity -> O(3n)
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
