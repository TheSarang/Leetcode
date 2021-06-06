class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        dp = [[] for i in range(len(s)+1)]
        wordDict = set(wordDict)
        dp[0] = [""]
        for i in range(1, len(dp)):
            res = []
            for j in range(i):
                word = s[j:i]
                if word in wordDict:
                    for prev in dp[j]:
                        res.append((prev + " " + word).strip())
            dp[i] = res
        return dp[-1]
