class Solution:
    def trap(self, height: 'List[int]') -> 'int':
        l,r=0,len(height)-1 #最左、最右端
        h1,h2=0,0 #记录左侧、右侧峰值
        ans=0
        while l<r:
            if height[l]<height[r]: # 选择较矮的一端
                if height[l]>h1:
                    h1=height[l] # 更新峰值
                else:
                    ans+=h1-height[l] # 累加结果
                l+=1
            else:
                if height[r]>h2:
                    h2=height[r] # 更新峰值
                else:
                    ans+=h2-height[r] # 累加结果
                r-=1
        return ans
        
# Runtime: 40 ms, faster than 99.98% of Python3 online submissions for Trapping Rain Water.
# Memory Usage: 13.6 MB, less than 5.11% of Python3 online submissions for Trapping Rain Water
