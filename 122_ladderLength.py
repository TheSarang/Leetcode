from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
#       TC = O(N*M^2)
#       SC = O(N*M^2)

        if endWord not in wordList:
            return 0
        
        L = len(beginWord)
        q1 = deque()
        q1.append((beginWord, 1))
        visited = set()
        visited.add(beginWord)
        dict_ = {}
        for word in wordList:
            for i in range(L):
                temp_word = word[:i] + '*' + word[i+1:]
                if temp_word not in dict_:
                    dict_[temp_word] = [word]
                else:
                    dict_[temp_word].append(word)
                    
        print(dict_)            
        while q1:
            current_word, step = q1.popleft()
            if current_word == endWord:
                return step
            for i in range(L):
                intermediate_word = current_word[:i] + '*' + current_word[i+1:]
                if intermediate_word in dict_:
                    for word in dict_[intermediate_word]:
                        if word not in visited:
                            q1.append((word, step + 1))
                            visited.add(word)
                    dict_[intermediate_word] = []
        return 0
        
#         -----------------------------------
        
        # TC = O(N * 27*M^2)
        # SC = O(N)
#          N = len of wordList
#          M = 27 
#          k = len of words in wordList
#         if endWord not in wordList:
#             return 0
    
#         q1 = deque()
#         q1.append((beginWord, 1))
#         visited = set()
#         visited.add(beginWord)
#         while q1:
#             word_, step = q1.popleft()
#             if word_ == endWord:
#                 return step
#             alphas = 'abcdefghijklmnopqrstuvwxyz'
#             for alpha in alphas:
#                 for i in range(len(word_)):
#                     temp_word = word_[:i] + alpha + word_[i+1:]
#                     if temp_word in wordList and temp_word not in visited:
#                         q1.append((temp_word, step + 1))
#                         visited.add(temp_word)
#         return 0
                
        
