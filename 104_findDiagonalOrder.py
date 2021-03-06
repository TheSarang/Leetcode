import collections
class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        
        res = []
        q = collections.deque()
        q.append((0,0))
        while q:
            row, col = q.popleft()
            if col == 0 and row < len(nums)-1:
                q.append((row + 1, col))
            if col< len(nums[row])-1:
                q.append((row, col+1))
            res.append(nums[row][col])
        return res
        
        
        
