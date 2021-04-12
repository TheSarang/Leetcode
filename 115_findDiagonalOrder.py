import collections
class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        dict_ = {}
        if not matrix: return []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i+j not in dict_:
                    dict_[i+j] = [matrix[i][j]]
                else:
                    dict_[i+j].append(matrix[i][j])
        for k in dict_.keys():
            if k%2 != 1:
                dict_[k].reverse()
            res += dict_[k]
        return res
