class Solution:
    def longestPalindrome(self, s: str) -> int:
        dict = {}
        sum = 0
        flag = True
        for i in s:
            if i not in dict:
                dict[i] = 1
            else:
                dict[i] += 1
        for i in dict:
            if (dict[i] %2 == 0):
                sum += dict[i]
            elif dict[i] > 1:
                sum += dict[i]  - 1
        for j in dict:
            if dict[j] %2 != 0:
                sum = sum + 1
                break
        return sum
        
