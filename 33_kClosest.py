class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        summ = 0
        dict = {}
        array1 = []
        for i in points:
            for j in i:
                summ += (0-j)**2
            if summ not in dict:
                dict[summ] = [i]
            else:
                dict[summ].append(i)
            summ = 0
        array2 = []
        for key in sorted(dict.keys()):
            if K == 0:
                break
            if len(dict[key]) <= K:
                array2.extend(dict[key])
                K -= len(dict[key])
            else:
                array2.extend(key[1])
        return array2
