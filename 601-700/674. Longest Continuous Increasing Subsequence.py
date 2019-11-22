'''
Given an unsorted array of integers, find the length of longest continuous increasing subsequence (subarray).

Example 1:
Input: [1,3,5,4,7]
Output: 3
Explanation: The longest continuous increasing subsequence is [1,3,5], its length is 3. 
Even though [1,3,5,7] is also an increasing subsequence, it's not a continuous one where 5 and 7 are separated by 4. 

Example 2:
Input: [2,2,2,2,2]
Output: 1
Explanation: The longest continuous increasing subsequence is [2], its length is 1. 

Note: Length of the array will not exceed 10,000.
'''

class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        start_idx = [0]
        for i in range(1, len(nums)):
            if nums[i-1] >= nums[i]:
                start_idx.append(i)
        start_idx.append(len(nums))
        return max(b - a for a, b in zip(start_idx, start_idx[1:]))
# Runtime: 76 ms, faster than 96.83% of Python3 online submissions for Longest Continuous Increasing Subsequence.
# Memory Usage: 13.8 MB, less than 100.00% of Python3 online submissions for Longest Continuous Increasing Subsequence.
