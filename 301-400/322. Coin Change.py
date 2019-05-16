'''
You are given coins of different denominations and a total amount of money amount. 
Write a function to compute the fewest number of coins that you need to make up that amount. 
If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:
Input: coins = [1, 2, 5], amount = 11
Output: 3 
Explanation: 11 = 5 + 5 + 1

Example 2:
Input: coins = [2], amount = 3
Output: -1

Note:
You may assume that you have an infinite number of each kind of coin.
'''

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + [float('inf')] * amount
        # 动态规划：f(amount) = min(f(amount-coin1),f(amount-coin2),...) + 1
        for idx in range(1, amount+1):
            dp[idx] = min(dp[idx - c] if idx - c >= 0 else float('inf')
                          for c in coins) + 1
        return (dp[-1], -1)[dp[-1] == float('inf')]
# Runtime: 1032 ms, faster than 78.18% of Python3 online submissions for Coin Change.
# Memory Usage: 13.2 MB, less than 68.67% of Python3 online submissions for Coin Change.
