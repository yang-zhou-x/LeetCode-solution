class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        aux=collections.Counter(S)
        ans=0
        for j in J:
            ans+=aux[j] # key不存在时返回0
        return ans
