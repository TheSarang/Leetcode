from queue import Queue
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = Queue()
        minutes = 0
        flag = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    # print([i,j])
                    queue.put([i,j])
        print(queue)
        if queue.empty():
            flag = 1
        
        while not queue.empty():
            size = queue.qsize()
            print(minutes)
            # print(size)
            for i in range(0,size):
                cur = queue.get()
                for pair in self._helper():
                    temp = [cur[0] + pair[0], cur[1] + pair[1]]
                    if 0 <= temp[0] < len(grid) and 0 <= temp[1] < len(grid[0]):
                        if grid[temp[0]][temp[1]] == 1:
                            queue.put([temp[0], temp[1]])
                            grid[temp[0]][temp[1]] = 2
            minutes +=1
        minutes -=1
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1
        if flag == 1:
            return 0
        return minutes
                
    def _helper(self):
        return [[0,1],[1,0],[0,-1],[-1,0]]
