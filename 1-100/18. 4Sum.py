'''
Given an array nums of n integers and an integer target, 
are there elements a, b, c, and d in nums such that a + b + c + d = target? 
Find all unique quadruplets in the array which gives the sum of target.

Note:
The solution set must not contain duplicate quadruplets.

Example:
Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.
A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
'''

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        results = []

        def findNsum(nums, target, N, prefix):
            nums.sort()
            # early stop and recursion base case
            if len(nums) < N or N < 2 or \
                    target < nums[0] * N or target > nums[-1] * N:
                return
            # 2sum problem
            if N == 2:
                l, r = 0, len(nums)-1
                while l < r:
                    s = nums[l] + nums[r]
                    if s == target:
                        results.append(prefix + [nums[l], nums[r]])
                        l += 1
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
                    elif s < target:
                        l += 1
                    else:
                        r -= 1
            else:
            # reduce N
                for i in range(len(nums) - N + 1):
                    if i == 0 or \
                            i > 0 and nums[i - 1] != nums[i]:
                        # recursive case
                        findNsum(nums[i + 1:], target - nums[i],
                                 N - 1, prefix + [nums[i]])

        findNsum(nums, target, 4, [])
        return results
# Runtime: 88 ms, faster than 92.22% of Python3 online submissions for 4Sum.
# Memory Usage: 13.2 MB, less than 75.80% of Python3 online submissions for 4Sum.
