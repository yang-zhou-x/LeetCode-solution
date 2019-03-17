class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        return math.factorial(m+n-2)//(math.factorial(m-1)*math.factorial(n-1))

# Runtime: 32 ms, faster than 99.23% of Python3 online submissions for Unique Paths.
