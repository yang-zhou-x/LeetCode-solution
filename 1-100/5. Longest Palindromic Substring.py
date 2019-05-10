'''
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:
Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:
Input: "cbbd"
Output: "bb"
'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ''

        def expand_center(s, left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1  # 从中心向外扩展
                right += 1
            return right - left - 1  # 子串长度

        start, end = 0, 0
        for i in range(len(s)):
            len1 = expand_center(s, i, i)  # 奇数长度时，即中心在某个字母处
            len2 = expand_center(s, i, i + 1)  # 偶数长度时，即中心在两个字母之间
            len12 = max(len1, len2)
            if len12 > end - start:
                start = i - (len12 - 1) // 2  # 确定起始位置
                end = i + len12 // 2
        return s[start:end + 1]
        
# Runtime: 892 ms, faster than 75.84% of Python3 online submissions for Longest Palindromic Substring.
# Memory Usage: 12.9 MB, less than 27.78% of Python3 online submissions for Longest Palindromic Substring.      
