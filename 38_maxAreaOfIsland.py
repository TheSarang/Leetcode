class Solution:
    def calculate(self, i, j, grid):
            if 0<=i<len(grid) and 0<=j<len(grid[i]) and grid[i][j] == 1:
                self.temp+=1
                grid[i][j] = '#'
                self.calculate(i+1, j, grid)
                self.calculate(i, j+1, grid)
                self.calculate(i-1, j, grid)
                self.calculate(i, j-1, grid)
                
                if self.temp >= self.maxNum:
                    self.maxNum = self.temp 
                    
                    
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.temp = 0
        self.maxNum = 0
             
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    self.calculate(i, j, grid)
                    self.temp = 0
        return self.maxNum
                    
            
            
