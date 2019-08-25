'''
Implement function ToLowerCase() that has a string parameter str, 
and returns the same string in lowercase.

Example 1:
Input: "Hello"
Output: "hello"

Example 2:
Input: "here"
Output: "here"

Example 3:
Input: "LOVELY"
Output: "lovely"
'''

class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        return str.lower()


class Solution:
    def toLowerCase(self, str: str) -> str:
        ans = ''
        for s in str:
            if ord(s) < 97:
                ans += chr(ord(s) + 32)
            else:
                ans += s
        return ans
# Runtime: 36 ms, faster than 62.30% of Python3 online submissions for To Lower Case.
# Memory Usage: 13.8 MB, less than 6.25% of Python3 online submissions for To Lower Case.
