'''
There are two sorted arrays nums1 and nums2 of size m and n respectively.
Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
You may assume nums1 and nums2 cannot be both empty.

Example 1:
nums1 = [1, 3]
nums2 = [2]
The median is 2.0

Example 2:
nums1 = [1, 2]
nums2 = [3, 4]
The median is (2 + 3)/2 = 2.5
'''

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        # 判断长度为偶数还是奇数
        if (m+n) % 2 == 0:
            isEven = True
            mid = (m+n)//2-1
        else:
            isEven = False
            mid = (m+n)//2
        # 合并数组
        left1, left2, left = 0, 0, 0
        nums = [0]*(m+n)
        while left1 < m and left2 < n:  # 从前向后
            if nums1[left1] < nums2[left2]:
                nums[left] = nums1[left1]
                left1 += 1
            else:
                nums[left] = nums2[left2]
                left2 += 1
            left += 1
        while left1 < m:
            nums[left] = nums1[left1]
            left1 += 1
            left += 1
        while left2 < n:
            nums[left] = nums2[left2]
            left2 += 1
            left += 1
        # 获取中位数
        if isEven:
            return (nums[mid]+nums[mid+1])/2
        else:
            return float(nums[mid])
# Runtime: 64 ms, faster than 94.62% of Python3 online submissions for Median of Two Sorted Arrays.
# Memory Usage: 13.5 MB, less than 5.11% of Python3 online submissions for Median of Two Sorted Arrays.


# 核心思路相同的另一种写法。
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)-1
        n = len(nums2)-1
        tot = m+n+1
        # 延长nums1作为新数组
        nums1 += [0]*(n+1)
        # 判断长度的奇偶
        if len(nums1) % 2 == 0:
            isEven = True
            mid = len(nums1)//2-1
        else:
            isEven = False
            mid = len(nums1)//2
        # 将nums2合并到nums1中
        while m >= 0 and n >= 0:  # 从后向前
            if nums1[m] > nums2[n]:
                nums1[tot] = nums1[m]
                m -= 1
            else:
                nums1[tot] = nums2[n]
                n -= 1
            tot -= 1
        while m >= 0:
            nums1[tot] = nums1[m]
            m -= 1
            tot -= 1
        while n >= 0:
            nums1[tot] = nums2[n]
            n -= 1
            tot -= 1
        # 获取中位数
        if isEven:
            return (nums1[mid]+nums1[mid+1])/2
        else:
            return float(nums1[mid])
# Runtime: 64 ms, faster than 94.62% of Python3 online submissions for Median of Two Sorted Arrays.
# Memory Usage: 13.5 MB, less than 5.11% of Python3 online submissions for Median of Two Sorted Arrays.
