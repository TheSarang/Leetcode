# Time Complexity: O(N*3^L) where N is the number of cells in the board and L is the length of the word to be matched.
# Space Complexity: O(L) where LLL is the length of the word to be matched.

class Solution:
    def __init__(self):
        self.res = False
        
    def dfs(self, i, j, board, word, path, k):
        if path == word:
            self.res = True
            return 
        
        if 0<=i<len(board) and 0<=j<len(board[0]) and board[i][j] == word[k]:
            temp = board[i][j]
            board[i][j] = '#'
            self.dfs(i+1, j, board, word, path + temp, k + 1)
            self.dfs(i-1, j, board, word, path + temp, k + 1)
            self.dfs(i, j+1, board, word, path + temp, k + 1)
            self.dfs(i, j-1, board, word, path + temp, k + 1)
            board[i][j] = temp
            
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(board)
        m = len(board[0])
        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    self.dfs(i, j, board, word,'', 0)
                    
        return self.res
