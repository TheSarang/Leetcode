class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        n = len(matrix) + 1
        m = len(matrix[0]) + 1
        if not matrix:
            return 0
        dp = [[0 for i in range(m)] for _ in range(n)]
        maxLen = 0
        for i in range(1, n):
            for j in range(1, m):
                if matrix[i-1][j-1] == '1':
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
                    maxLen = max(maxLen, dp[i][j])
        return maxLen * maxLen
        
