'''
Say you have an array for which the ith element is the price of a given stock on day i.
If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock),
design an algorithm to find the maximum profit.
Note that you cannot sell a stock before you buy one.

Example 1:
Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.

Example 2:
Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
'''

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy = float('inf')
        ans = 0
        for p in prices:
            if p < buy:
                buy = p
            else:
                if p-buy > ans:
                    ans = p - buy
        return ans
# Runtime: 20 ms, faster than 100.00% of Python online submissions for Best Time to Buy and Sell Stock.
# Memory Usage: 11.5 MB, less than 64.80% of Python online submissions for Best Time to Buy and Sell Stock.
 
# 其他写法。python3
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        res = [0] * len(prices)
        lowest = prices[0]
        for i in range(1, len(prices)):
            if prices[i] <= lowest:
                lowest = prices[i]
            else:
                res[i] = prices[i] - lowest
        return max(res)
# Runtime: 36 ms, faster than 99.78% of Python3 online submissions for Best Time to Buy and Sell Stock.
# Memory Usage: 14.1 MB, less than 5.08% of Python3 online submissions for Best Time to Buy and Sell Stock.

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = float('inf')
        profit = 0
        for p in prices:
            if p < buy:
                buy = p
            else:
                if p - buy > profit:
                    profit = p - buy
        return profit
# Runtime: 32 ms, faster than 99.64% of Python3 online submissions for Best Time to Buy and Sell Stock.
# Memory Usage: 14.1 MB, less than 23.68% of Python3 online submissions for Best Time to Buy and Sell Stock.
