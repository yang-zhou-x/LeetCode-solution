class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
        ans=0
        prev=1000
        for ss in s:
            ans+=d[ss]
            if prev<d[ss]:
                ans-=prev*2
            prev=d[ss]
        return ans
        
