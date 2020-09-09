class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        temp = ""
        j = 0
        for i in range(0, len(t)):
            if j < len(s): 
                if t[i] == s[j]:
                    temp += t[i]
                    i+=1
                    j+=1
                elif t[i] != s[j]:
                    i+=1
        print(temp)
        return s == temp
