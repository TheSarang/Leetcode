class Solution:
    def isHappy(self, n: int) -> bool:
        sett = set()
        summ = n
        while summ!= 1:
            temp = 0
            string = str(summ)
            for i in string:
                temp += int(i)**2
            summ = temp
            if temp in sett:
                return False
            sett.add(temp)
        return True
