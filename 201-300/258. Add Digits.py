'''
Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

Example:
Input: 38
Output: 2 
Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2. 
             Since 2 has only one digit, return it.

Follow up:
Could you do it without any loop/recursion in O(1) runtime?
'''

class Solution:
    def addDigits(self, num: int) -> int:
        if num < 10:
            return num
        s = str(num)
        while len(s) > 1:
            s = str(sum(int(x) for x in s))
        return int(s)
# Runtime: 40 ms, faster than 58.33% of Python3 online submissions for Add Digits.
# Memory Usage: 13.8 MB, less than 5.26% of Python3 online submissions for Add Digits.

class Solution:
    def addDigits(self, num: int) -> int:
        while num > 9:
            num = sum(divmod(num, 10))
        return num
# Runtime: 28 ms, faster than 99.73% of Python3 online submissions for Add Digits.
# Memory Usage: 14.1 MB, less than 5.26% of Python3 online submissions for Add Digits.
