class Solution:
    def firstUniqChar(self, s: str) -> int:
        dict1 = {}
        for i in s:
            if i not in dict1.keys():
                dict1[i] = 1
            else:
                dict1[i] += 1
 
        for (i, v) in dict1.items():
            if v == 1:
                return s.find(i)
        return -1
