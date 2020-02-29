class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(grid, i,j):
            if (0<=i<len(grid)) and (0<=j<len(grid[i])) and (grid[i][j] == '1'):
                grid[i][j] = '#'
                dfs(grid, i+1,j)
                dfs(grid, i,j+1)
                dfs(grid, i-1,j)
                dfs(grid, i,j-1)
            
        islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    dfs(grid, i,j)
                    islands += 1
        
        return islands
