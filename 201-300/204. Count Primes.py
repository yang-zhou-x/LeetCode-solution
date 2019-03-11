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
