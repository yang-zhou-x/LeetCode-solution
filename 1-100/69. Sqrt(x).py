class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        r=x
        while r*r>x:
            r=(r+x/r)//2
        return r
        
# Runtime: 28 ms, faster than 96.64% of Python online submissions for Sqrt(x).
# Memory Usage: 11 MB, less than 5.37% of Python online submissions for Sqrt(x).
