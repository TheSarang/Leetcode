class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        starting_times = sorted([intervals[i][0] for i in range(len(intervals))])
        end_times = sorted([intervals[i][1] for i in range(len(intervals))])
        L = len(intervals)
        used_rooms = start_point = end_point = 0
        while start_point < L:
            if starting_times[start_point] >= end_times[end_point]:
                used_rooms -= 1
                end_point += 1
            used_rooms += 1
            start_point += 1
        return used_rooms
        
