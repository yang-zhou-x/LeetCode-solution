'''
Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

Example 1:
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true

Example 2:
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false
'''

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        dp = [[True] * (len(s2) + 1) for _ in range(len(s1) + 1)]
        for j in range(1, len(s2) + 1):  # 第1行。s3前段全部取自s2
            if dp[0][j - 1] and s2[j - 1] == s3[j - 1]:
                dp[0][j] = True
            else:
                dp[0][j] = False

        for i in range(1, len(s1) + 1):  # 第1列。s3前段全部取自s1
            if dp[i - 1][0] and s1[i - 1] == s3[i - 1]:
                dp[i][0] = True
            else:
                dp[i][0] = False

        for i in range(1, len(s1) + 1):  # 余下的格子
            for j in range(1, len(s2) + 1):
                if dp[i - 1][j] and s1[i - 1] == s3[i + j - 1] or\
                        dp[i][j - 1] and s2[j - 1] == s3[i + j - 1]:
                    dp[i][j] = True
                else:
                    dp[i][j] = False
        return dp[-1][-1]
# Runtime: 32 ms, faster than 98.08% of Python3 online submissions for Interleaving String.
# Memory Usage: 14 MB, less than 16.67% of Python3 online submissions for Interleaving String.
