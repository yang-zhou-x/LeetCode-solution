class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def bs_left(A, x):
            left, right = 0, len(A) - 1
            while left <= right:
                mid = (left + right) // 2
                if x <= A[mid]:  # x=A[mid]时，继续向左移动
                    right = mid - 1
                else: 
                    left = mid + 1
            return left

        def bs_right(A, x):
            left, right = 0, len(A) - 1
            while left <= right:
                mid = (left + right) // 2
                if x >= A[mid]:   # x=A[mid]时，继续向右移动
                    left = mid + 1
                else: 
                    right = mid - 1
            return right

        left = bs_left(nums, target)
        right = bs_right(nums, target)
        return (left, right) if left <= right else [-1, -1]

# Runtime: 20 ms, faster than 99.97% of Python online submissions for Find First and Last Position of Element in Sorted Array.
# Memory Usage: 11.4 MB, less than 36.09% of Python online submissions for Find First and Last Position of Element in Sorted Array.
