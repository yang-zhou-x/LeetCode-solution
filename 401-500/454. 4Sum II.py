class Solution:
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        ans=0
        AB=collections.Counter(a+b for a in A for b in B)
        for c,d in itertools.product(C,D):
            try:
                ans+=AB[-c-d]
            except:
                pass
        
        return ans
                
# Runtime: 316 ms, faster than 63.99% of Python3 online submissions for 4Sum II.
