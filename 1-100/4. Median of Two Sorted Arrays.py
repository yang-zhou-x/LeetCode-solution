class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m=len(nums1)
        n=len(nums2)
        # 判断长度为偶数还是奇数
        if (m+n)%2==0:
            isEven=True
            mid=(m+n)//2-1
        else:
            isEven=False
            mid=(m+n)//2
        # 合并数组
        left1,left2,left=0,0,0
        nums=[0]*(m+n)
        while left1<m and left2<n:
            if nums1[left1]<nums2[left2]:
                nums[left]=nums1[left1]
                left1+=1
            else:
                nums[left]=nums2[left2]
                left2+=1
            left+=1
        while left1<m:
            nums[left]=nums1[left1]
            left1+=1
            left+=1
        while left2<n:
            nums[left]=nums2[left2]
            left2+=1
            left+=1
        # 获取中位数
        if isEven:
            return (nums[mid]+nums[mid+1])/2
        else:
            return float(nums[mid])

# Runtime: 64 ms, faster than 94.62% of Python3 online submissions for Median of Two Sorted Arrays.
# Memory Usage: 13.5 MB, less than 5.11% of Python3 online submissions for Median of Two Sorted Arrays.        
