class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n:
            count += n & 1  # 按位操作符
            n >>= 1  # 按位操作符
        return count
        
# Runtime: 20 ms, faster than 95.99% of Python online submissions for Number of 1 Bits.
# Memory Usage: 10.7 MB, less than 64.97% of Python online submissions for Number of 1 Bits.
