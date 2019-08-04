'''
Given a string which contains only lowercase letters, 
remove duplicate letters so that every letter appear once and only once. 
You must make sure your result is the smallest in lexicographical order among all possible results.
Example 1:
Input: "bcabc"
Output: "abc"
Example 2:
Input: "cbacdcbc"
Output: "acdb"
'''

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        if not s:
            return s
        ss = set(s)
        for ch in sorted(ss):
            suffix = s[s.index(ch):]
            if set(suffix) == ss:
                return ch + self.removeDuplicateLetters(suffix.replace(ch, ''))
# Runtime: 52 ms, faster than 37.74% of Python3 online submissions for Remove Duplicate Letters.
# Memory Usage: 13.8 MB, less than 8.33% of Python3 online submissions for Remove Duplicate Letters.


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        rindex = {c: i for i, c in enumerate(s)}
        result = ''
        for i, c in enumerate(s):
            if c not in result:
                while c < result[-1:] and i < rindex[result[-1]]:
                    result = result[:-1]
                result += c
        return result
# Runtime: 36 ms, faster than 97.17% of Python3 online submissions for Remove Duplicate Letters.
# Memory Usage: 13.8 MB, less than 8.33% of Python3 online submissions for Remove Duplicate Letters.
