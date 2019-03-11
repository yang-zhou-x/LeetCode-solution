class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i,l,r=0,0,len(nums)-1  # l的位置放0，r的位置放2
        while i<=r:
            if nums[i]==0:  # 遇到0时
                nums[l],nums[i]=nums[i],nums[l]  # 移到l位置。exchange操作
                l+=1
                i+=1
            elif nums[i]==2:  # 遇到2时
                nums[i],nums[r]=nums[r],nums[i]  # 移到r位置。exchange操作
                r-=1
            else:
                i+=1
                
# Runtime: 36 ms, faster than 97.81% of Python3 online submissions for Sort Colors.
