'''
Given a string, your task is to count how many palindromic substrings in this string.
The substrings with different start indexes or end indexes are counted 
as different substrings even they consist of same characters.

Example 1:
Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
 
Example 2:
Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
 
Note:
The input string length won't exceed 1000.
'''

class Solution:
    def countSubstrings(self, s: str) -> int:
        if not s:
            return 0
        count = 0

        def expand_center(left, right):
            while left >= 0 and right < len(s):
                if s[left] == s[right]:
                    nonlocal count
                    count += 1
                    left -= 1
                    right += 1
                else:
                    break
        for i in range(len(s)):
            expand_center(i, i)
            expand_center(i, i+1)
        return count
# Runtime: 136 ms, faster than 68.40% of Python3 online submissions for Palindromic Substrings.
# Memory Usage: 13 MB, less than 85.04% of Python3 online submissions for Palindromic Substrings.

# 另一种写法
class Solution:
    def countSubstrings(self, s: str) -> int:
        if not s:
            return 0

        def expand_center(left, right):
            count = 0
            while left >= 0 and right < len(s):
                if s[left] == s[right]:
                    count += 1
                    left -= 1
                    right += 1
                else:
                    return count
            return count
        ans = 0
        for i in range(len(s)):
            ans += expand_center(i, i)
            ans += expand_center(i, i+1)
        return ans
# Runtime: 132 ms, faster than 74.64% of Python3 online submissions for Palindromic Substrings.
# Memory Usage: 13.1 MB, less than 75.02% of Python3 online submissions for Palindromic Substrings.
