class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        aux=set()
        for a in A:
            if a in aux:
                return a
            else:
                aux.add(a)
                
