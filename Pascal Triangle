class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        elif numRows == 2:
            return [[1],[1,1]]
        else:
            finalList = [[1]]
            flag = True
            i=2
            while i < numRows:
                j = 0;k = 1;
                d = numRows - i
                if flag:
                    finalList.append([1,1])
                    flag = False
                    continue
                list2 = []
                list2.append(finalList[0][0])
                z = 1
                while z+d < numRows:
                    if d > 0:
                        if j <= i:
                            list2.append(finalList[i-1][j] + finalList[i-1][j+1])
                        d+=1
                        j+=1
                    else:
                        break
                list2.append(finalList[0][0])
                finalList.append(list2)
                i+=1
            return finalList
            
