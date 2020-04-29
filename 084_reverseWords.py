class Solution:
    def reverseWords(self, s: str) -> str:
        str = ""
        for i in s.split(" "):
            str+=i[::-1] + " "
        return str.strip()
            
            
