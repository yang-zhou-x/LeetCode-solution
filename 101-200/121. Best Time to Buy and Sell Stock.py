class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy=float('inf')
        ans=0
        for p in prices:
            if p<buy:
                buy=p
            else:
                if p-buy>ans:
                    ans=p-buy
        return ans
    
    
# Runtime: 20 ms, faster than 100.00% of Python online submissions for Best Time to Buy and Sell Stock.
# Memory Usage: 11.5 MB, less than 64.80% of Python online submissions for Best Time to Buy and Sell Stock.
 
