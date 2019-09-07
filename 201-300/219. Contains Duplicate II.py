'''
Given an array of integers and an integer k, 
find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] 
and the absolute difference between i and j is at most k.

Example 1:
Input: nums = [1,2,3,1], k = 3
Output: true

Example 2:
Input: nums = [1,0,1,1], k = 1
Output: true

Example 3:
Input: nums = [1,2,3,1,2,3], k = 2
Output: false
'''

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        pos = {}
        for i,n in enumerate(nums):
            if n in pos:
                if i - pos[n] <= k:
                    return True
                pos[n] = i
            else:
                pos[n] = i
        return False
# Runtime: 108 ms, faster than 69.76% of Python3 online submissions for Contains Duplicate II.
# Memory Usage: 21.4 MB, less than 43.75% of Python3 online submissions for Contains Duplicate II.
