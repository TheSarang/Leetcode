class Solution:
    def isPalindrome(self, s: str) -> bool:
        ###Sarang Narkhede###

        # BASIC
        # TIME COMPLEXITY: O(N)
        # SPACE COMPLEXITY: O(N)
        res = ""
        for c in s:
            if c.isalnum():
                res += c.lower()
        
        # res[::-1] will consume more memory
        return res == res[::-1]

        # OPTIMIZED
        # TIME COMPLEXITY: O(N)
        # SPACE COMPLEXITY: O(1)

        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not self.numAlpha(s[l]):
                l += 1
            while r > l and not self.numAlpha(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1

        return True

    def numAlpha(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or 
        ord('a') <= ord(c) <= ord('z') or 
        ord('0') <= ord(c) <= ord('9'))       

