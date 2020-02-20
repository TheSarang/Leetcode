class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        size = len(A)
        
        if size < 3:
            return False

        for i in range( 1, size ):
            if A[i] > A[i-1]:continue
            elif A[ i ] == A[ i-1 ]:return False
            else:
                if i == 1:return False
                else:break   
        
        for j in range( i, size):
            if A[j] < A[j-1]:
                continue
            else:return False
        else:
            return True
        
