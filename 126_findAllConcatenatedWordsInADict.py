class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        def wordbreak(word, prewords):
            if not prewords:
                return False
            dp = [False for i in range(len(word) + 1)]
            dp[0] = True
            
            for i in range(len(dp)):
                for j in range(i):
                    if dp[j] and word[j:i] in prewords:
                        dp[i] = True
                        break
            return dp[-1]
        
        res = []
        words.sort(key=len)
        prewords = set()
        for word in words:
            if wordbreak(word, prewords):
                res.append(word)
            prewords.add(word)
        return res
    
    
        
            
