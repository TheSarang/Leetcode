 class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        sarang = 0
        def dfs(i,j,grid):
            if (0<=i<len(grid)) and (0<=j<len(grid[i])) and (grid[i][j] == 0):
                grid[i][j] = 1
                dfs(i+1,j,grid)
                dfs(i,j+1,grid)
                dfs(i-1,j,grid)
                dfs(i,j-1,grid)
            
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 0 and (i == 0 or i == len(grid) - 1 or j == 0 or j == len(grid[0])-1):
                    dfs(i,j,grid)
                    
                    
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 0:
                    dfs(i,j,grid)
                    sarang+=1
        return sarang
