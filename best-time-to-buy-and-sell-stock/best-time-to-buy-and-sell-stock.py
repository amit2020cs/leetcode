class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit, lowest = 0, float('inf')
        for price in prices:
            max_profit = max(price - lowest, max_profit)
            lowest = min(lowest, price)
        return max_profit