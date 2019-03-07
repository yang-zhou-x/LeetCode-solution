class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        for i,a in enumerate(A):
            a.reverse()
            A[i]=[1-x for x in a]
        return A
        
