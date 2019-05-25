'''
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
You are given a target value to search. If found in the array return its index, otherwise return -1.
You may assume no duplicate exists in the array.
Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
'''

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left+right) >> 1
            # 找到target时
            if nums[mid] == target:
                return mid
            # left到mid为升序时
            if nums[left] <= nums[mid]:
                # 落入有序段
                if nums[left] <= target <= nums[mid]:
                    right = mid-1
                else:
                    left = mid+1
            # left到mid乱序，即mid到right为升序
            else:
                # 落入有序段
                if nums[mid] <= target <= nums[right]:
                    left = mid+1
                else:
                    right = mid-1
        return -1
# Runtime: 28 ms, faster than 99.68% of Python3 online submissions for Search in Rotated Sorted Array.
# Memory Usage: 13.3 MB, less than 43.83% of Python3 online submissions for Search in Rotated Sorted Array.
