class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        count = 1
        intervals.sort(key = lambda x: x[0])
        heap = []
        heapq.heappush(heap, intervals[0][1])
        for i in range(1, len(intervals)):
            pair = intervals[i]
            if pair[0] >= heap[0]:
                heapq.heappushpop(heap, pair[1])
            else:
                heapq.heappush(heap, pair[1])                
        return len(heap)
    
#     ----------------------------------------------------------
    
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
