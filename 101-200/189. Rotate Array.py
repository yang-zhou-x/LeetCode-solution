'''
Given an array, rotate the array to the right by k steps, where k is non-negative.

Example 1:
Input: [1,2,3,4,5,6,7] and k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

Example 2:
Input: [-1,-100,3,99] and k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]

Note:
Try to come up as many solutions as you can, 
there are at least 3 different ways to solve this problem.
Could you do it in-place with O(1) extra space?
'''

class Solution:
    def rotate(self, nums: 'List[int]', k: 'int') -> 'None':
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        nums[:] = nums[-k:]+nums[:-k]  # 必须加[:]
# Runtime: 40 ms, faster than 99.96% of Python3 online submissions for Rotate Array.
# Memory Usage: 13.4 MB, less than 74.85% of Python3 online submissions for Rotate Array.

# 20190821
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        nums[:] = nums[-k:]+nums[:-k]
# Runtime: 64 ms, faster than 98.18% of Python3 online submissions for Rotate Array.
# Memory Usage: 15.3 MB, less than 5.09% of Python3 online submissions for Rotate Array.
