import collections
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        dict = collections.defaultdict(int)
        finalList = []
        for val in cpdomains:
            key = val.split(' ')[1]
            val = int(val.split(' ')[0])
            dict[key] += val
        
            tempKey = ""
            for i in range(len(key) - 1, 0, -1):
                if key[i] == '.':
                    dict[tempKey] += val
                tempKey = key[i] + tempKey
        
        
        for key, val in dict.items():
            temp = str(val) + " " + str(key)
            finalList.append(temp)
        return finalList
        
