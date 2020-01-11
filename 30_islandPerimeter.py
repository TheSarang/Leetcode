class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        def check(grid, i, j):
            nums_of_sides = 0
            left, right, top, bottom = True, True, True, True
            
            if i == 0:
                top = False
            if i == len(grid) - 1:
                bottom = False
            if j == 0:
                left = False
            if j == len(grid[i]) - 1:
                right = False
                
            # if (0<i<len(grid)) and (0<j<len(grid[i])) and (grid[i][j] == 1):
            if bottom and grid[i+1][j] == 1:
                nums_of_sides+=1
            if right and grid[i][j+1] == 1:
                nums_of_sides+=1
            if top and grid[i-1][j] == 1:
                nums_of_sides+=1
            if left and grid[i][j-1] == 1:
                nums_of_sides+=1

            return (4-nums_of_sides)
            
        summ = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    summ+=int(check(grid, i, j))
        return summ
