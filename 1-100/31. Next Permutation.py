'''
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).
The replacement must be in-place and use only constant extra memory.

Here are some examples. 
Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
'''

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if nums:
            right = len(nums) - 1
            while right > 0 and nums[right - 1] >= nums[right]:
                right -= 1  # nums尾部，降序排列的起始位置
            idx = right - 1  # 尾部，第一个中断降序排列的数
            if idx < 0:  # nums降序排列。如[3,2,1] -> [1,2,3]
                nums.reverse()
            else:
                while right < len(nums) and nums[right] > nums[idx]:
                    right += 1
                nums[idx], nums[right - 1] = nums[right - 1], nums[idx]
                # reverse
                nums[idx + 1:] = reversed(nums[idx + 1:])
# Runtime: 44 ms, faster than 63.28% of Python3 online submissions for Next Permutation.
# Memory Usage: 13.2 MB, less than 53.27% of Python3 online submissions for Next Permutation.
