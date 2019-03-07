class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        letters=''.join(chr(x) for x in range(ord('a'),ord('z')+1))
        ans=len(s)
        for l in letters:
            idx=s.find(l)
            if idx!=-1 and idx==s.rfind(l):
                ans=min(ans,idx)
        return [ans,-1][ans==len(s)]
        
        
# Runtime: 20 ms, faster than 100.00% of Python online submissions for First Unique Character in a String.
# Memory Usage: 11 MB, less than 86.51% of Python online submissions for First Unique Character in a String.
 
