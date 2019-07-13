'''
Given an array nums of n integers and an integer target, 
find three integers in nums such that the sum is closest to target. 
Return the sum of the three integers. 
You may assume that each input would have exactly one solution.

Example:
Given array nums = [-1, 2, 1, -4], and target = 1.
The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
'''

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if len(nums) < 4:
            return sum(nums)
        nums.sort()
        ans = sum(nums[:3])
        dist = abs(ans - target)
        for i in range(len(nums) - 2):
            j, k = i + 1, len(nums) - 1
            while j < k:
                tmp = nums[i] + nums[j] + nums[k]
                if tmp == target:
                    return tmp
                dist_tmp = abs(tmp - target)
                if dist_tmp < dist:
                    ans = tmp
                    dist = dist_tmp
                if tmp < target:
                    j += 1
                else:
                    k -= 1
        return ans
# Runtime: 112 ms, faster than 69.58% of Python3 online submissions for 3Sum Closest.
# Memory Usage: 13.2 MB, less than 40.07% of Python3 online submissions for 3Sum Closest.
