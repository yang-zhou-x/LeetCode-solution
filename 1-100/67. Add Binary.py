'''
Given two binary strings, return their sum (also a binary string).
The input strings are both non-empty and contains only characters 1 or 0.

Example 1:
Input: a = "11", b = "1"
Output: "100"

Example 2:
Input: a = "1010", b = "1011"
Output: "10101"
'''

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if not a or not b:
            return a or b
        if a[-1] == '1' and b[-1] == '1':
            return self.addBinary(self.addBinary(a[:-1], b[:-1]), '1') + '0'
        if a[-1] == '0' and b[-1] == '0':
            return self.addBinary(a[:-1], b[:-1]) + '0'
        else:
            return self.addBinary(a[:-1], b[:-1]) + '1'
# Runtime: 44 ms, faster than 44.62% of Python3 online submissions for Add Binary.
# Memory Usage: 13.6 MB, less than 5.41% of Python3 online submissions for Add Binary.
