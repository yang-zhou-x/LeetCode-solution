class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start=0
        ans=0
        aux={}
        for i,ss in enumerate(s):
            if ss in aux and start<=aux[ss]:
                start=aux[ss]+1
                aux[ss]=i
            else:
                ans=max(ans,i-start+1)
                aux[ss]=i
        return ans
