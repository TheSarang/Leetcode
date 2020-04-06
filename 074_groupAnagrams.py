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
