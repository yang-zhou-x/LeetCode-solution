class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k=k%len(nums)
        nums[:]=nums[-k:]+nums[:-k]
            
# Runtime: 44 ms, faster than 100.00% of Python3 online submissions for Rotate Array.
# Memory Usage: 12.9 MB, less than 12.46% of Python3 online submissions for Rotate Array.
