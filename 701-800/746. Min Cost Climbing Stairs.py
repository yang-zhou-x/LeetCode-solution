'''
On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).
Once you pay the cost, you can either climb one or two steps. You need to find minimum cost 
to reach the top of the floor, and you can either start from the step with index 0, or the step with index 1.

Example 1:
Input: cost = [10, 15, 20]
Output: 15
Explanation: Cheapest is start on cost[1], pay that cost and go to the top.

Example 2:
Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
Output: 6
Explanation: Cheapest is start on cost[0], and only step on 1s, skipping cost[3].

Note:
cost will have a length in the range [2, 1000].
Every cost[i] will be an integer in the range [0, 999].
'''

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) < 2:
            return
        if len(cost) == 2:
            return min(cost)
        dp = [0] * len(cost)
        dp[0], dp[1] = cost[0], cost[1]
        for i in range(2, len(cost) - 1):
            dp[i] = min(dp[i-1], dp[i-2]) + cost[i]
        dp[-1] = min(dp[-2], dp[-3] + cost[-1])
        return dp[-1]
# Runtime: 68 ms, faster than 64.42% of Python3 online submissions for Min Cost Climbing Stairs.
# Memory Usage: 13.7 MB, less than 7.69% of Python3 online submissions for Min Cost Climbing Stairs.
