class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = list(set(nums)) + [0]
        n = len(nums)
        for i in range(len(nums)):  # 无用元素赋值为0
            if nums[i] < 0 or nums[i] >= n:
                nums[i] = 0
        for i in range(len(nums)):  # 使用hash来记录
            nums[nums[i] % n] += n
        for i in range(1, len(nums)):
            if nums[i] // n == 0:
                return i
        return n
# Runtime: 36 ms, faster than 99.35% of Python3 online submissions for First Missing Positive.
# Memory Usage: 13.2 MB, less than 5.26% of Python3 online submissions for First Missing Positive.
