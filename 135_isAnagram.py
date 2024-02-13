class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # Time Complexity: O(n)
        # Space Complexity: O(n)
        
        res = dict()
      
        for alpha in s:
            if alpha in res:
                res[alpha] += 1
            else:
                res[alpha] = 1

        for alpha in t:
            if alpha in res:
                res[alpha] -= 1
            else:
                return False

        for vals in res.values():
            if vals != 0:
                return False
              
        return True
        
        

