'''
Given an integer array, you need to find one continuous subarray 
that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order, too.
You need to find the shortest such subarray and output its length.

Example 1:
Input: [2, 6, 4, 8, 10, 9, 15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.

Note:
Then length of the input array is in range [1, 10,000].
The input array may contain duplicates, so ascending order here means <=.
'''
# 解法1：慢
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        cmax, cmin = -float('inf'), float('inf')
        l, r = 0, -1  # 这样赋值是为了结果为0的情形
        for i in range(n):
            cmax = max(cmax, nums[i])  # 从左向右遍历
            cmin = min(cmin, nums[n - 1 - i])  # 从右向左遍历
            if nums[i] != cmax:  # 第i个数应该是nums[:i+1]中最大的
                r = i  # r是最右侧的不符合的位置。
            if nums[n - 1 - i] != cmin:  # 第n-1-i个数应该是nums[n-1-i:]中最小的
                l = n - 1 - i  # l是最左侧的不符合的位置。
        return r - l + 1
# Runtime: 120 ms, faster than 32.24% of Python3 online submissions for Shortest Unsorted Continuous Subarray.
# Memory Usage: 14.1 MB, less than 7.77% of Python3 online submissions for Shortest Unsorted Continuous Subarray.

# 解法2：快
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        left, right, maxIndex = None, 0, 0
        for i in range(1, len(nums)):
            if nums[i] >= nums[maxIndex]:
                maxIndex = i
            else:
                right = i
                if left is None:
                    left = i-1
                while left > 0 and nums[left-1] > nums[i]:
                    left -= 1
        return right-left+1 if left is not None else 0
# Runtime: 52 ms, faster than 99.76% of Python3 online submissions for Shortest Unsorted Continuous Subarray.
# Memory Usage: 14.1 MB, less than 74.32% of Python3 online submissions for Shortest Unsorted Continuous Subarray.
