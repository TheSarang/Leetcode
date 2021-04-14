class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = 0
        dict_ = {}
        count = 0
        maxLen = 0
        for i in range(len(s)):
            if s[i] in dict_ and j <= dict_[s[i]]:
                j = dict_[s[i]] + 1
            dict_[s[i]] = i
            count =  i - j + 1
            print(count)
            maxLen = max(count, maxLen)
        return maxLen
