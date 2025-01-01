# Modified Kadane's algorithm
# TC: O(n)
# SC: O(1)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if prices == []:
            return  0
        buy_stock = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            if buy_stock > prices[i]:
                buy_stock = prices[i]
                
            profit = max(prices[i] - buy_stock, profit)
        return (profit)
