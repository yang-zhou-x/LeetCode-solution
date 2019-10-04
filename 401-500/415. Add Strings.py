'''
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:
The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
'''

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        n1, n2 = 0, 0
        for n in num1:
            n1 = n1 * 10 + int(n)
        for n in num2:
            n2 = n2 * 10 + int(n)
        return str(n1 + n2)
# Runtime: 56 ms, faster than 37.32% of Python3 online submissions for Add Strings.
# Memory Usage: 13.8 MB, less than 5.55% of Python3 online submissions for Add Strings.
