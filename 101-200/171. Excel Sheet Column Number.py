'''
Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:
    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
    ...

Example 1:
Input: "A"
Output: 1

Example 2:
Input: "AB"
Output: 28

Example 3:
Input: "ZY"
Output: 701
'''

# 类似于26进制数
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

class Solution:
    def titleToNumber(self, s: str) -> int:
        ans = 0
        for cha in s:
            ans = ans * 26 + ord(cha) - 64  # ord('A') - 64 == 1
        return ans
# Runtime: 28 ms, faster than 99.06% of Python3 online submissions for Excel Sheet Column Number.
# Memory Usage: 14 MB, less than 9.09% of Python3 online submissions for Excel Sheet Column Number.
