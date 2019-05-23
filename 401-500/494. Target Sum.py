'''
You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. 
Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.
Find out how many ways to assign symbols to make sum of integers equal to target S.

Example 1:
Input: nums is [1, 1, 1, 1, 1], S is 3. 
Output: 5
Explanation: 
-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3
There are 5 ways to assign symbols to make the sum of nums be target 3.

Note:
The length of the given array is positive and will not exceed 20.
The sum of elements in the given array will not exceed 1000.
Your output answer is guaranteed to be fitted in a 32-bit integer.
'''

class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        if not nums:
            return 0
        cache = {nums[0]: 1, -nums[0]: 1} if nums[0] != 0 else {0: 2}
        for i in range(1, len(nums)):
            tmp = {}
            for c in cache:
                # 总数 = tmp中已有的个数+新增的个数
                tmp[c+nums[i]] = tmp.get(c+nums[i], 0)+cache.get(c)
                tmp[c-nums[i]] = tmp.get(c-nums[i], 0)+cache.get(c)
            cache = tmp
        return cache.get(S, 0)
# Runtime: 328 ms, faster than 55.32% of Python3 online submissions for Target Sum.
# Memory Usage: 13.2 MB, less than 78.38% of Python3 online submissions for Target Sum.
