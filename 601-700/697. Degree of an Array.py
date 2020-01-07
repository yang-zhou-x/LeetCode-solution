'''
Given a non-empty array of non-negative integers nums, 
the degree of this array is defined as the maximum frequency of any one of its elements.

Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.

Example 1:
Input: [1, 2, 2, 3, 1]
Output: 2
Explanation: 
The input array has a degree of 2 because both elements 1 and 2 appear twice.
Of the subarrays that have the same degree:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
The shortest length is 2. So return 2.

Example 2:
Input: [1,2,2,3,1,4,2]
Output: 6

Note:
nums.length will be between 1 and 50,000.
nums[i] will be an integer between 0 and 49,999.
'''

from collections import Counter

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        freq = Counter(nums)
        max_freq = max(freq.values())
        candidates = []
        for num in freq:
            if freq[num] == max_freq:
                candidates.append(num)
        ans = float('inf')
        rev_nums = list(reversed(nums))
        for num in candidates:
            tmp = len(nums) - nums.index(num) - rev_nums.index(num)
            if tmp < ans:
                ans = tmp
        return ans
# Runtime: 620 ms, faster than 11.88% of Python3 online submissions for Degree of an Array.
# Memory Usage: 14 MB, less than 45.45% of Python3 online submissions for Degree of an Array.

# 改进
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        cnt = {}
        left = {}
        right = {}
        for i, n in enumerate(nums):
            if n not in left:
                left[n] = i
            right[n] = i
            cnt[n] = cnt.get(n, 0) + 1
        max_freq = max(cnt.values())
        ans = len(nums)
        for n in cnt:
            if cnt[n] == max_freq and right[n] - left[n] + 1 < ans:
                ans = right[n] - left[n] + 1
        return ans
# Runtime: 236 ms, faster than 91.02% of Python3 online submissions for Degree of an Array.
# Memory Usage: 13.9 MB, less than 81.82% of Python3 online submissions for Degree of an Array.
