class Solution:
    def fib(self, N: int) -> int:
        a,b = 0,1
        for _ in range(N):
            a, b = b, a+b
        return a 
