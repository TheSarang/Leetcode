import re
class Solution:
    def removeDuplicates(self, S: str) -> str:
        while re.findall(r'(.)\1',S):
            S = re.sub(r'(.)\1', '',S)
        return S
