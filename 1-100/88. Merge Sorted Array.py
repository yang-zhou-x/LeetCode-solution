class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        right1=m-1  # 末尾位置
        right2=n-1
        right=m+n-1
        while right1>=0 and right2>=0:
            if nums1[right1]>nums2[right2]:
                nums1[right]=nums1[right1]
                right1-=1
            else:
                nums1[right]=nums2[right2]
                right2-=1
            right-=1
        while right2>=0:
            nums1[right]=nums2[right2]
            right2-=1
            right-=1
        
# Runtime: 36 ms, faster than 99.02% of Python3 online submissions for Merge Sorted Array.
# Memory Usage: 12.6 MB, less than 29.52% of Python3 online submissions for Merge Sorted Array.
