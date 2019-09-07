'''
You are a professional robber planning to rob houses along a street. 
Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. 
That means the first house is the neighbor of the last one. 
Meanwhile, adjacent houses have security system connected and it will automatically contact the police 
if two adjacent houses were broken into on the same night.
Given a list of non-negative integers representing the amount of money of each house, 
determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:
Input: [2,3,2]

Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2),
             because they are adjacent houses.

Example 2:
Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
'''

class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) < 4:
            return max(nums)
        
        def rob(nums):  # 非环的情况
            dp = [0] * (len(nums) + 1)
            dp[1] = nums[0]
            for i in range(2, len(dp)):
                dp[i] = max(dp[i-1], dp[i-2]+nums[i-1])
            return dp[-1]
        
        return max(rob(nums[1:]), nums[0]+rob(nums[2:-1]))
# Runtime: 40 ms, faster than 51.03% of Python3 online submissions for House Robber II.
# Memory Usage: 13.6 MB, less than 5.56% of Python3 online submissions for House Robber II.
