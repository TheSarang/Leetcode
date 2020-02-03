class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key = lambda x: x[0])
        if intervals == []:
            return []
        result = [intervals[0]]
        i = 1
        j = 0
        while i < len(intervals):
            if intervals[i][0] <= result[j][1]:
                result[j][1] = max(intervals[i][1], result[j][1])
            else:
                result.append(intervals[i])
                j+=1
            i+=1
        return (result)
            
            
