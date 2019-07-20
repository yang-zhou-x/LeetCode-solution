'''
Given a sorted array and a target value, 
return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:
Input: [1,3,5,6], 5
Output: 2

Example 2:
Input: [1,3,5,6], 2
Output: 1

Example 3:
Input: [1,3,5,6], 7
Output: 4

Example 4:
Input: [1,3,5,6], 0
Output: 0
'''

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) >> 1
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # 此时left == right
        # if nums[left] == target:
        #     return left
        # elif nums[left] > target:
        #     return left
        # else:
        #     return left + 1
        if nums[left] < target:
            return left + 1
        else: 
            return left
# Runtime: 68 ms, faster than 6.79% of Python3 online submissions for Search Insert Position.
# Memory Usage: 14.4 MB, less than 5.12% of Python3 online submissions for Search Insert Position.

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return bisect.bisect_left(nums, target)
# Runtime: 52 ms, faster than 6.79% of Python3 online submissions for Search Insert Position.
# Memory Usage: 14.4 MB, less than 5.12% of Python3 online submissions for Search Insert Position.
