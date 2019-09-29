'''
Given an array of integers and an integer k, you need to find the total 
number of continuous subarrays whose sum equals to k.

Example 1:
Input:nums = [1,1,1], k = 2
Output: 2

Note:
The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].
'''

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return int(nums[0] == k)
        ans = 0
        cache = {0:1}
        cumulation = 0
        for n in nums:
            cumulation += n
            if cumulation - k in cache:
                ans += cache[cumulation-k]
            cache[cumulation] = cache.get(cumulation, 0) + 1
        return ans
# Runtime: 128 ms, faster than 75.27% of Python3 online submissions for Subarray Sum Equals K.
# Memory Usage: 16 MB, less than 20.00% of Python3 online submissions for Subarray Sum Equals K.
