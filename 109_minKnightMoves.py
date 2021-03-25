import collections
class Solution:
    def minKnightMoves1(self, x: int, y: int) -> int:
        q = collections.deque([[0, 0, 0]])
        visited = set([(0,0)])
        x = abs(x)
        y = abs(y)
        while q:
            a, b, step = q.popleft()
            if a == x and b == y:
                return step
            for dx, dy in [[1,2], [2,1], [-1,2], [2,-1], [1,-2], [-2, 1]]:
                if (a+dx, b+dy) not in visited and -1 <= a+dx <= x+2 and -1 <= b+dy <= y+2:
                    visited.add((a+dx, b+dy))
                    q.append([a+dx, b+dy, step+1])
        return -1

    #  extra for loop for level wise traversal. in above code, i am using step hence no need to create extra for loop
    def minKnightMoves2(self, x: int, y: int) -> int:
        q = collections.deque([[0, 0, 0]])
        visited = set([(0, 0)])
        x = abs(x)
        y = abs(y)
        while q:
            n = len(q)
            for i in range(n):
                a, b, step = q.popleft()
                if a == x and b == y:
                    return step
                for dx, dy in [[1, 2], [2, 1], [-1, 2], [2, -1], [1, -2], [-2, 1]]:
                    if (a + dx, b + dy) not in visited and -1 <= a + dx <= x + 2 and -1 <= b + dy <= y + 2:
                        visited.add((a + dx, b + dy))
                        q.append([a + dx, b + dy, step + 1])
        return -1
def main():
    sol = Solution()
    print(sol.minKnightMoves2(5,5))

if __name__ == '__main__':
    main()
