class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
         
        def dfs(grid, i, j):
            if 0 <= i < len(grid) and 0 <= j < len(grid[i]) and grid[i][j] == 0:
                grid[i][j] = -1
                dfs(grid, i + 1, j)
                dfs(grid, i, j + 1)
                dfs(grid, i, j - 1)
                dfs(grid, i - 1, j)
        
        islands = 0
        for i in range(len(grid)):
            n = len(grid)
            for j in range(len(grid[i])):
                a = len(grid[i])
                if grid[i][j] == 0 and (i==0 or i==n-1) and ((j==0 or j==a-1)):
                    dfs(grid, i, j)
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 0:
                    dfs(grid, i, j)
                    islands += 1        
        return islands
