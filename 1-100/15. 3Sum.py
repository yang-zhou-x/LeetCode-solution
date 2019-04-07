class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 排序
        nums.sort()
        # 
        ans=[]
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:# 去重
                continue
            target=-nums[i] # 另2个数之和
            left,right=i+1,len(nums)-1
            while left<right:
                if nums[left]+nums[right]==target: # 满足条件时
                    ans.append([nums[i],nums[left],nums[right]])
                    left+=1
                    while left<right and nums[left]==nums[left-1]: # 去重
                        left+=1
                elif nums[left]+nums[right]<target:
                    left+=1
                else:
                    right-=1
        return ans
# Runtime: 1024 ms, faster than 52.52% of Python3 online submissions for 3Sum.
# Memory Usage: 16.7 MB, less than 23.23% of Python3 online submissions for 3Sum.

# 改进后的算法，用dict来记录
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        # 计数
        count = collections.Counter(nums)
        ans = []
        # 对key排序，即对去重后的数字排序
        keys = sorted(count)
        for i,n in enumerate(keys):
            # 计数大于等于2 
            if count[n] >= 2:
                if n == 0 and count[n] >= 3: # 特殊情况：0
                    ans.append([0,0,0])
                else:
                    complement = -2*n
                    if complement in count and complement != n: # 排除特殊情况：0
                        ans.append([n,n] + [complement])
            # 小于0
            if n < 0:
                twosum = -n # 另两数之和
                left = bisect.bisect_left(keys, twosum - keys[-1], i+1) # 获取左侧索引
                right = bisect.bisect_right(keys, twosum // 2, left) # 获取右侧索引
                for j in keys[left:right]:
                    complement = twosum - j
                    if complement in count and complement != j:
                        ans.append([n,j,complement])
        return ans
# Runtime: 292 ms, faster than 99.62% of Python3 online submissions for 3Sum.
# Memory Usage: 17.6 MB, less than 8.99% of Python3 online submissions for 3Sum.
