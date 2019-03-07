class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans=0
        for ss in s:
            ans=ans*26+ord(ss)-64  # -64=-ord('A')+1
        return ans

# 类似于26进制数
