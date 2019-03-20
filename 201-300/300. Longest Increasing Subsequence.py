class Solution:
    def lengthOfLIS(self, nums: 'List[int]') -> 'int':
        ans=[]
        for n in nums: #动态规划
            idx=self.bs(ans,n)
            if idx==len(ans):
                ans.append(n) #尾部添加1个数
            else:
                ans[idx]=n #替换掉最小的那个大于（含等于）n的数
        return len(ans)
    
    def bs(self,ans,n): #二分查找
        l,r=0,len(ans)-1
        while l<=r:
            m=(l+r)//2
            if n<ans[m]:
                r=m-1
            elif ans[m]<n:
                l=m+1
            else:
                return m
        return l
                
# Runtime: 60 ms, faster than 73.09% of Python3 online submissions for Longest Increasing Subsequence.
# Memory Usage: 13.3 MB, less than 5.81% of Python3 online submissions for Longest Increasing Subsequence.
