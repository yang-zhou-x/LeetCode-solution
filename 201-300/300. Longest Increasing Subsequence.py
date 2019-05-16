'''
Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:
Input: [10,9,2,5,3,7,101,18]
Output: 4 
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 

Note:
There may be more than one LIS combination, it is only necessary for you to return the length.
Your algorithm should run in O(n2) complexity.

Follow up: Could you improve it to O(n log n) time complexity?
'''

class Solution:
    def lengthOfLIS(self, nums: 'List[int]') -> 'int':
        ans = []
        for n in nums:
            idx = self.bs(ans, n)
            if idx == len(ans):
                ans.append(n)  # 尾部添加1个数
            else:
                ans[idx] = n  # 替换掉最小的那个大于（含等于）n的数
        return len(ans)

    def bs(self, ans, n):  # 二分查找
        left, right = 0, len(ans)-1
        while left <= right:
            mid = (left+right)//2
            if n < ans[mid]:
                right = mid-1
            elif ans[mid] < n:
                left = mid+1
            else:
                return mid
        return left
# Runtime: 40 ms, faster than 90.95% of Python3 online submissions for Longest Increasing Subsequence.
# Memory Usage: 13.2 MB, less than 66.47% of Python3 online submissions for Longest Increasing Subsequence.

# 借助build-in模块
class Solution:
    def lengthOfLIS(self, nums: 'List[int]') -> 'int':
        dp = []
        for n in nums:
            idx = bisect.bisect_left(dp, n)
            if idx < len(dp):
                dp[idx] = n
            else:
                dp.append(n)
        return len(dp)
# Runtime: 36 ms, faster than 98.30% of Python3 online submissions for Longest Increasing Subsequence.
# Memory Usage: 13.3 MB, less than 37.83% of Python3 online submissions for Longest Increasing Subsequence.
