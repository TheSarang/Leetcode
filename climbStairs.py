class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=2:
            return n
        tempArray = [0]*(n+1)
        tempArray[1], tempArray[2] = 1,2
        for i in range(3, len(tempArray)):
            tempArray[i] = tempArray[i-2] + tempArray[i-1]
        
        return tempArray[n]
        
