class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        unwrap = list(zip(*strs))
        res=""
        for element in unwrap:
            if len(set(element)) == 1:
                res += element[0]
            else:
                break
        return res
