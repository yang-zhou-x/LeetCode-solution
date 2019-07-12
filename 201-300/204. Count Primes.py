'''
Count the number of prime numbers less than a non-negative number, n.

Example:
Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
'''

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<2:
            return 0
        import numpy as np
        ans=np.ones(n,dtype=np.bool)
        ans[:2]=False
        for i in range(2,int(n**0.5)+1):
            if ans[i]:
                ans[i*i:n:i]=False  # i的倍数都不是素数
        return int(np.sum(ans))
# Runtime: 48 ms, faster than 99.89% of Python online submissions for Count Primes.
# Memory Usage: 22.1 MB, less than 97.13% of Python online submissions for Count Primes.

# python3
class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        ans = [True] * n
        ans[:2] = [False] * 2  # 0和1不是素数
        for i in range(2, int(n ** 0.5) + 1):
            if ans[i]:
                ans[i * i::i] = [False] * len(ans[i * i::i])
        return sum(ans)
# Runtime: 228 ms, faster than 84.11% of Python3 online submissions for Count Primes.
# Memory Usage: 36.5 MB, less than 26.95% of Python3 online submissions for Count Primes.
