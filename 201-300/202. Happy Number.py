class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        cache=set()
        while n!=1:
            if n in cache:
                return False
            cache.add(n)
            n=sum(int(x)**2 for x in str(n))
        return True
        
# Runtime: 24 ms, faster than 91.81% of Python online submissions for Happy Number.
# Memory Usage: 10.8 MB, less than 27.56% of Python online submissions for Happy Number.
 
