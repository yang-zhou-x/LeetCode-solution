'''
Given an array of n positive integers and a positive integer s, 
find the minimal length of a contiguous subarray of which the sum ≥ s. 
If there isn't one, return 0 instead.

Example: 
Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.

Follow up:
If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n). 
'''

class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums:
            return 0
        left, right = 0, 1  # 含左端点，不含右端点
        ans = float('inf')
        curr_sum = nums[0]
        while right <= len(nums) and left < right:
            if curr_sum >= s:
                ans = min(right - left, ans)
                curr_sum -= nums[left]
                left += 1
            else:
                if right < len(nums):
                    curr_sum += nums[right]
                right += 1
        return ans if ans != float('inf') else 0
# Runtime: 88 ms, faster than 64.23% of Python3 online submissions for Minimum Size Subarray Sum.
# Memory Usage: 16.4 MB, less than 7.69% of Python3 online submissions for Minimum Size Subarray Sum.
