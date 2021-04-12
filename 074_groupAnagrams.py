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

   
import collections
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_ = collections.defaultdict(list)
        for val in strs:
            dict_[tuple(sorted(val))].append(val)
        return dict_.values()
