'''
Given a string s and a string t, check if s is subsequence of t.
You may assume that there is only lower case English letters in both s and t. 
t is potentially a very long (length ~= 500,000) string, and s is a short string (<=100).
A subsequence of a string is a new string which is formed from the original string 
by deleting some (can be none) of the characters without disturbing the relative positions 
of the remaining characters. (ie, "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:
s = "abc", t = "ahbgdc"
Return true.

Example 2:
s = "axc", t = "ahbgdc"
Return false.

Follow up:
If there are lots of incoming S, say S1, S2, ... , Sk where k >= 1B, 
and you want to check one by one to see if T has its subsequence. In this scenario, how would you change your code?

Credits:
Special thanks to @pbrother for adding this problem and creating all test cases.
'''

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        if not t:
            return False
        left_s = 0
        for cha in t:
            if s[left_s] == cha:
                left_s += 1
            if left_s == len(s):
                return True
        return False
# Runtime: 172 ms, faster than 53.94% of Python3 online submissions for Is Subsequence.
# Memory Usage: 18.5 MB, less than 26.67% of Python3 online submissions for Is Subsequence.

# 改进方法
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        if not t:
            return False
        for cha in s:
            idx = t.find(cha)
            if idx == -1:
                return False
            t = t[idx + 1:]
        return True
# Runtime: 36 ms, faster than 97.50% of Python3 online submissions for Is Subsequence.
# Memory Usage: 18.2 MB, less than 26.67% of Python3 online submissions for Is Subsequence.
