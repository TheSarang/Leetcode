class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        rows = len(board)
        cols = len(board[0])
        
        neighbors = [[1,0],[-1,0],[0,1],[0,-1],[1,1],[1,-1],[-1,1],[-1,-1]]
        
        res = [[board[row][col] for col in range(cols)] for row in range(rows)]
        for row in range(rows):
            for col in range(cols):
                live_cells = 0
                for neib in neighbors:
                    r = row + neib[0]
                    c = col + neib[1]
                    
                    if (r >= 0 and r < rows) and (c >=0 and c < cols) and res[r][c] == 1:
                        live_cells +=1
                        
                if res[row][col] == 1 and (live_cells < 2 or live_cells > 3):
                    board[row][col] = 0
                    
                elif res[row][col] == 0 and live_cells == 3:
                    board[row][col] = 1
           
