class Solution:
    def maxArea(self, height: 'List[int]') -> 'int':
        l,r=0,len(height)-1
        ans=0
        while l<r:
            ans=max(min(height[l],height[r])*(r-l),ans)
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return ans
        
# Runtime: 60 ms, faster than 85.52% of Python3 online submissions for Container With Most Water.
# Memory Usage: 13.7 MB, less than 21.61% of Python3 online submissions for Container With Most Water.
