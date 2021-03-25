from collections import deque

# Time complexity: O(rows * cols) -> each cell is visited at least once
# Space complexity: O(rows * cols) -> in the worst case if all the oranges are rotten they will be added to the queue

class Solution:
    def orangesRotting1(self, grid):
        rows = len(grid)
        if rows == 0:
            return -1
        cols = len(grid[0])
        fresh_cnt = 0
        rotten = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    rotten.append((r, c))
                elif grid[r][c] == 1:
                    fresh_cnt += 1
        minutes_passed = 0
        while rotten and fresh_cnt > 0:
            minutes_passed += 1
            for _ in range(len(rotten)):
                x, y = rotten.popleft()
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    xx, yy = x + dx, y + dy
                    if xx < 0 or xx == rows or yy < 0 or yy == cols:
                        continue
                    if grid[xx][yy] == 0 or grid[xx][yy] == 2:
                        continue
                    fresh_cnt -= 1
                    grid[xx][yy] = 2
                    rotten.append((xx, yy))

        return minutes_passed if fresh_cnt == 0 else -1

    #  extra for loop for level wise traversal. in below code, i am using number_of_minutes in queue hence no need to create extra for loop
    def orangesRotting2(self, grid: List[List[int]]) -> int:
        number_of_minutes = 0
        fresh_oranges = 0
        q = collections.deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh_oranges += 1
                elif grid[i][j] == 2:
                    q.append((i, j, 1))

        while q and fresh_oranges > 0:
            dx, dy, number_of_minutes = q.popleft()
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for i, j in directions:
                if 0 <= dx + i < len(grid) and 0 <= dy + j < len(grid[0]) and grid[dx + i][dy + j] == 1:
                    q.append((dx + i, dy + j, number_of_minutes + 1))
                    fresh_oranges -= 1
                    grid[dx + i][dy + j] = 2

        return number_of_minutes if fresh_oranges == 0 else -1

def main():
    sol = Solution()
    matrix = [[2,1,1],[1,1,0],[0,1,1]]
    print(sol.orangesRotting1(matrix))

if __name__ == '__main__':
    main()
