class Solution:
    def maxArea(self, height: List[int]) -> int:
        MaxVal = 0
        x1 = len(height) - 1
        x0 = 0
        while x1 != x0:
            if height[x1] >= height[x0]:
                area = (x1-x0) * height[x0]
                x0+=1
            else:
                area = (x1-x0) * height[x1]
                x1-=1
            MaxVal = max(MaxVal, area)
        return MaxVal
