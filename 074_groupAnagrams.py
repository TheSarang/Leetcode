class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dicts = {}
        for word in strs:
            key = tuple(sorted(word))
            if key not in dicts:
                dicts[key] = [word]
            else:
                dicts[key].append(word)
        return (dicts.values())
------------------------------------------------------------
   
import collections
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_ = collections.defaultdict(list)
        for val in strs:
            dict_[tuple(sorted(val))].append(val)
        return dict_.values()

------------------------------------------------------------

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]::
        res = {}
        for s in strs:
            word = self._helper(s)
            if word not in res:
                res[word] = [s]
            else:
                res[word].append(s)

        return res.values()
        
    def _helper(self, word):
        alpha_array = [0] * 26
        res = ""
        for c in word:
            alpha_array[ord(c) - ord("a")] += 1
        
        for i in range(len(alpha_array)):
            if alpha_array[i] != 0:
                res += str(chr(ord("a") + i)) + str(alpha_array[i])
        
        return res
