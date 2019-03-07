class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        ans=0
        idx=0
        while idx<len(prices)-1:
            if prices[idx]<prices[idx+1]:
                ans+=prices[idx+1]-prices[idx]
            idx+=1
        return ans
     
# 另一种方法
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        ans=0
        idx=0
        while idx<len(prices)-1:
            while idx<len(prices)-1 and prices[idx]>=prices[idx+1]:
                idx+=1
            valley=prices[idx]
            while idx<len(prices)-1 and prices[idx]<prices[idx+1]:
                idx+=1
            peak=prices[idx]
            ans+=peak-valley
        return ans
        
