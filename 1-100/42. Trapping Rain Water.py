class Solution:
    def trap(self, height: 'List[int]') -> 'int':
        l,r=0,len(height)-1
        h1,h2=0,0
        ans=0
        while l<r:
            if height[l]<height[r]:
                if height[l]>h1:
                    h1=height[l]
                else:
                    ans+=h1-height[l]
                l+=1
            else:
                if height[r]>h2:
                    h2=height[r]
                else:
                    ans+=h2-height[r]
                r-=1
        return ans
        
# 
