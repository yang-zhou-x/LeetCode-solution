class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        cmax, cmin = -float('inf'), float('inf')
        l, r = 0, -1  # 这样赋值是为了结果为0的情形
        
        for i in range(n):
            cmax = max(cmax, nums[i])  # 从左向右遍历
            cmin = min(cmin, nums[n - 1 - i])  # 从右向左遍历
            if nums[i] != cmax:  # r是最右侧的不符合的位置。第i个数应该是nums[:i+1]中最大的
                r = i
            if nums[n - 1 - i] != cmin:  # l是最左侧的不符合的位置。第n-1-i个数应该是nums[n-1-i:]中最小的
                l = n - 1 - i
        return r - l + 1


# Runtime: 120 ms, faster than 32.24% of Python3 online submissions for Shortest Unsorted Continuous Subarray.
# Memory Usage: 14.1 MB, less than 7.77% of Python3 online submissions for Shortest Unsorted Continuous Subarray.
