'''
Given a non-negative integer n, count all numbers with unique digits, x, where 0 ≤ x < 10n.

Example:
Input: 2
Output: 91 
Explanation: The answer should be the total numbers in the range of 0 ≤ x < 100, 
             excluding 11,22,33,44,55,66,77,88,99
'''

class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        ans = 10
        if n == 1:
            return ans
        if n > 10:
            n = 10
        while n > 1:
            tmp = 1
            start = 9
            for i in range(n):
                if i == 0:
                    tmp *= start
                else:
                    tmp *= start
                    start -= 1
            ans += tmp
            n -= 1
        return ans
# Runtime: 36 ms, faster than 65.69% of Python3 online submissions for Count Numbers with Unique Digits.
# Memory Usage: 13.8 MB, less than 50.00% of Python3 online submissions for Count Numbers with Unique Digits.

# 略微改进
class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        if n == 1:
            return 10
        if n > 10:
            n = 10
        ans = 10
        tmp = 9
        base = 9
        while n > 1:
            tmp = tmp * base
            ans += tmp
            base -= 1
            n -= 1
        return ans
# Runtime: 32 ms, faster than 88.28% of Python3 online submissions for Count Numbers with Unique Digits.
# Memory Usage: 13.8 MB, less than 50.00% of Python3 online submissions for Count Numbers with Unique Digits.
