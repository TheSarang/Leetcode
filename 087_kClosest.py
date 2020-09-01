import math
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        return sorted(points, key=lambda x:math.sqrt(x[0]*x[0] + x[1]*x[1]))[:K]
                
