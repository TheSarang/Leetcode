class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        dp = [[0 for i in range(len(A))] for i in range(len(B))]
        maxNum = 0
        for i in range(len(A)):
            for j in range(len(B)):
                if A[i] == B[j]:
                    if i>0 and j>0:
                        dp[i][j] = dp[i-1][j-1] + 1
                    else:
                        dp[i][j] = 1
                maxNum = max(maxNum, dp[i][j])
        return maxNum
