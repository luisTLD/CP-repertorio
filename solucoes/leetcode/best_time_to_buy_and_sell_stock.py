# LeetCode - Best Time to Buy and Sell Stock
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        b = prices[0]
        ans = 0
        for p in prices:
            ans = max(ans, p - b)
            if p < b:
                b = p
        ans = max(ans, prices[len(prices) - 1] - b)
        return ans
