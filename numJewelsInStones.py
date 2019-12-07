class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        dict1 = {}
        for i in S:
            if i not in dict1.keys():
                dict1[i] = 1
            else:
                dict1[i] = dict1[i] + 1
        count = 0
        for i in J:
            if i in dict1.keys():
                count+=dict1[i]
            
            
        return count
