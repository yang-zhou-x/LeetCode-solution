'''
Say you have an array for which the ith element is the price of a given stock on day i.
Design an algorithm to find the maximum profit. 
You may complete as many transactions as you like (ie, buy one and sell one share 
of the stock multiple times) with the following restrictions:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)

Example:
Input: [1,2,3,0,2]
Output: 3 
Explanation: transactions = [buy, sell, cooldown, buy, sell]
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        dp = [[0, 0] for _ in range(len(prices)+1)]
        # dp[i][0] 不持有股票时
        # dp[i][1] 持有股票时
        dp[1][1] = -prices[0]
        for i in range(1, len(prices)):
            dp[i+1][0] = max(dp[i][0], dp[i][1]+prices[i])  # 延续不持有，或是刚卖出
            dp[i+1][1] = max(dp[i][1], dp[i-1][0]-prices[i])  # 延续持有，或是刚买入。买时cooldown一天。
        return max(dp[-1])
# Runtime: 40 ms, faster than 92.04% of Python3 online submissions for Best Time to Buy and Sell Stock with Cooldown.
# Memory Usage: 13.6 MB, less than 8.20% of Python3 online submissions for Best Time to Buy and Sell Stock with Cooldown.
