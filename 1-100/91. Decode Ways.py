'''
A message containing letters from A-Z is being encoded to numbers using the following mapping:
'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.

Example 1:
Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).

Example 2:
Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
'''

class Solution:
    def numDecodings(self, s: str) -> int:
        if not s:
            return 0
        dp=[0]*(len(s)+1)
        dp[0]=1
        # 公式为：
        # dp[i]=dp[i-1] if s[i] != '0'
        #        + dp[i-2] if '09'<s[i-2:i]<'27'
        for i in range(1,len(s)+1):
            if s[i-1]!='0':
                dp[i]=dp[i-1]
            if i>1 and '09'<s[i-2:i]<'27':
                dp[i]+=dp[i-2]
        return dp[-1]
        
# Runtime: 40 ms, faster than 94.30% of Python3 online submissions for Decode Ways.
# Memory Usage: 13.2 MB, less than 20.73% of Python3 online submissions for Decode Ways.
