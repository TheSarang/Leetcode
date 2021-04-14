class Solution(object):
    def findLength(self, A, B):
        n = len(A) + 1
        m = len(B) + 1
        dp = [[0 for i in range(m)] for i in range(n)]
        
        for i in range(1, n):
            for j in range(1, m):
                if A[i-1] == B[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
        
        
        return max([max(num) for num in dp])
                
