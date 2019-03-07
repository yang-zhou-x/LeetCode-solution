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
                if x > A[mid]: 
                    left = mid + 1
                else: 
                    right = mid - 1
            return left

        def bs_right(A, x):
            left, right = 0, len(A) - 1
            while left <= right:
                mid = (left + right) // 2
                if x >= A[mid]: 
                    left = mid + 1
                else: 
                    right = mid - 1
            return right

        left = bs_left(nums, target)
        right = bs_right(nums, target)
        return (left, right) if left <= right else [-1, -1]
