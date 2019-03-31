class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n==0:
            return 1
        if n<0:
            return 1/self.myPow(x,-n)
        if n%2:
            return x*self.myPow(x,n-1)
        else:
            return self.myPow(x*x,n/2)
            
# Runtime: 20 ms, faster than 96.13% of Python online submissions for Pow(x, n).
# Memory Usage: 10.8 MB, less than 38.57% of Python online submissions for Pow(x, n).
