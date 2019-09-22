'''
Given an array of integers and an integer k, you need to find the number of unique k-diff pairs in the array. 
Here a k-diff pair is defined as an integer pair (i, j), 
where i and j are both numbers in the array and their absolute difference is k.

Example 1:
Input: [3, 1, 4, 1, 5], k = 2
Output: 2
Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
Although we have two 1s in the input, we should only return the number of unique pairs.

Example 2:
Input:[1, 2, 3, 4, 5], k = 1
Output: 4
Explanation: There are four 1-diff pairs in the array, (1, 2), (2, 3), (3, 4) and (4, 5).

Example 3:
Input: [1, 3, 1, 5, 4], k = 0
Output: 1
Explanation: There is one 0-diff pair in the array, (1, 1).

Note:
The pairs (i, j) and (j, i) count as the same pair.
The length of the array won't exceed 10,000.
All the integers in the given input belong to the range: [-1e7, 1e7].
'''

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        # 空间复杂度较优
        nums.sort()
        left = 0
        cnt = 0
        right = len(nums) - 1
        while left < right:
            check = left + 1
            while check < len(nums) and nums[left] + k > nums[check]:
                check += 1
            if check == len(nums):
                left += 1
                continue
            if nums[left] + k == nums[check]:
                cnt += 1
            while left < right and nums[left] == nums[left + 1]:
                left += 1
            left += 1
        return cnt
# Runtime: 348 ms, faster than 12.51% of Python3 online submissions for K-diff Pairs in an Array.
# Memory Usage: 15.1 MB, less than 64.52% of Python3 online submissions for K-diff Pairs in an Array.


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        cache = {}
        for n in nums:
            cache[n] = cache.get(n, 0) + 1
        if k == 0:
            cnt = len(list(filter(lambda x: x > 1, cache.values())))
        elif k > 0:
            cnt = 0
            for key in cache:
                if key + k in cache:
                    cnt += 1
        else:
            cnt = 0
        return cnt
# Runtime: 140 ms, faster than 87.81% of Python3 online submissions for K-diff Pairs in an Array.
# Memory Usage: 15.3 MB, less than 61.29% of Python3 online submissions for K-diff Pairs in an Array.
