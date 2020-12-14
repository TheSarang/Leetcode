class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        res = 0
        for ch in s + t:
            res ^= ord(ch)
        return chr(res)
