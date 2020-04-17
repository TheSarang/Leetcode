class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        oneS = zeroS = finalD = 0
        for pair in shift:
            if pair[0] == 0:
                zeroS += pair[1]
            else:
                oneS += pair[1]
        if oneS > zeroS:
            finalD = 1
        diff = abs(zeroS - oneS)
        for pair in range(diff):
            print(s)
            if finalD == 1:
                temp = s[-1]
                s = s[:-1]
                s = temp + s
            elif finalD == 0:
                temp = s[0]
                s = s[1:]
                s = s + temp
            
        return s
        
