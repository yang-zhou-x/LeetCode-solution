class Solution:
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l,r=0,len(nums)-1
        while l<r:
            m=(l+r)//2  # 因为只需要返回1个peak，所以可以使用二分法查找。也可以顺序查找。
            if nums[m]>nums[m+1]:
                r=m  # 包含右侧点
            else:
                l=m+1
        
        return l
        
# Runtime: 32 ms, faster than 99.43% of Python3 online submissions for Find Peak Element.
