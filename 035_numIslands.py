from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        n = len(grid)
        m = len(grid[0])
        
        def dfs(i, j):
            if 0<=i<n and 0<=j<m and grid[i][j] == '1':
                grid[i][j] = 'X'
                dfs(i+1, j)
                dfs(i-1, j)
                dfs(i, j+1)
                dfs(i, j-1)
                
        
        def bfs(i, j):
            q1 = deque()  
            q1.append((i,j))
            while q1:
                dx, dy = q1.popleft() 
                directions = [[1,0],[0,1],[-1,0],[0,-1]]
                for (x, y) in directions:
                    xx = x + dx 
                    yy = y + dy
                    if 0<=xx<n and 0<=yy<m and grid[xx][yy] == '1':
                        q1.append((xx,yy))
                        grid[xx][yy] = 'X'
                        
                        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    # dfs(i, j)
                    bfs(i, j)
                    res+=1

        return res
