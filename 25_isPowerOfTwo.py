import math
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        a = (math.log2(n))
        print(str(a)[-1])
        if str(a)[-1] == '0':
            return True
        return False
