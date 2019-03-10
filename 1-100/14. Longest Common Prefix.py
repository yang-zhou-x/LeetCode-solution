class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        ans=strs[0]
        for s in strs[1:]:
            while not s.startswith(ans) and len(ans)>0:
                ans=ans[:-1]
        return ans
        
# Runtime: 16 ms, faster than 100.00% of Python online submissions for Longest Common Prefix.
# Memory Usage: 11.2 MB, less than 5.66% of Python online submissions for Longest Common Prefix.
