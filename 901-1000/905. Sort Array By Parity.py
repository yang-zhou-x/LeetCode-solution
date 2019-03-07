class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        even=[]
        odd=[]
        [even.append(x) if x%2==0 else odd.append(x) for x in A]
        return even+odd
        
