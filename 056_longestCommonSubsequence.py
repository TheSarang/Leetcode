class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n,m=len(text1),len(text2)
        dp=[[0 for _ in range(m+1)] for _ in range (n+1) ]
        for i in range(n):
            for j in range(m):
                if text1[i]==text2[j]:
                    dp[i+1][j+1]=dp[i][j]+1
                else:
                    dp[i+1][j+1]=max(dp[i][j+1],dp[i+1][j])
        return dp[-1][-1]
