class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start = [pair[0] for pair in sorted(intervals, key = lambda x: x[0])]
        end = [pair[1] for pair in sorted(intervals, key = lambda x: x[1])]
        start_idx = end_idx = 0
        res = 0
        while start_idx < len(start):
            if start[start_idx] < end[end_idx]:
                res += 1
            else:
                end_idx +=1
            start_idx += 1
        return res
        
