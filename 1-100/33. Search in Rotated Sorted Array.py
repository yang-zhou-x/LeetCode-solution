class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        left,right=0,len(nums)-1
        while left<=right:
            mid=(left+right)>>1
            # 找到target时
            if nums[mid]==target:
                return mid
            # left到mid为升序时
            if nums[left]<=nums[mid]:
                # 落入有序段
                if nums[left]<=target<=nums[mid]:
                    right=mid-1
                else:
                    left=mid+1
            # left到mid乱序，即mid到right为升序
            else:
                # 落入有序段
                if nums[mid]<=target<=nums[right]:
                    left=mid+1
                else:
                    right=mid-1
        return -1
# Runtime: 36 ms, faster than 99.24% of Python3 online submissions for Search in Rotated Sorted Array.
# Memory Usage: 13.2 MB, less than 5.96% of Python3 online submissions for Search in Rotated Sorted Array.
