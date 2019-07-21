'''
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', 
return the length of last word in the string.
If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

Example:
Input: "Hello World"
Output: 5
'''

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        res = s.split()
        return len(res[-1]) if res else 0
# Runtime: 36 ms, faster than 61.27% of Python3 online submissions for Length of Last Word.
# Memory Usage: 13.9 MB, less than 5.37% of Python3 online submissions for Length of Last Word.

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.rstrip()
        if len(s)  == 0:
            return 0
        i = 1
        while i <= len(s):
            if s[-i] != ' ':
                i += 1
            else:
                break
        return i - 1
# Runtime: 44 ms, faster than 12.02% of Python3 online submissions for Length of Last Word.
# Memory Usage: 13.8 MB, less than 5.37% of Python3 online submissions for Length of Last Word.
