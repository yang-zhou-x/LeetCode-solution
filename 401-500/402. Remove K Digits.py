'''
Given a non-negative integer num represented as a string, 
remove k digits from the number so that the new number is the smallest possible.

Note:
The length of num is less than 10002 and will be ≥ k.
The given num does not contain any leading zero.

Example 1:
Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.

Example 2:
Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.

Example 3:
Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and it is left with nothing which is 0.
'''

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        while k > 0:
            k -= 1
            i = 0
            while i < len(num) - 1:
                if num[i] > num[i + 1]:
                    break
                i += 1
            num = num[:i] + num[i + 1:]
        if len(num) == 0:
            return "0"
        else:
            return str(int(num))
# Runtime: 616 ms, faster than 10.30% of Python3 online submissions for Remove K Digits.
# Memory Usage: 13.9 MB, less than 16.80% of Python3 online submissions for Remove K Digits.

# 改进
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k == 0:
            return num
        if len(num) == k:
            return '0'
        i = 0
        while k > 0:
            while i + 1 < len(num) and num[i] <= num[i + 1]:
                i += 1
            num = num[:i] + num[i + 1:]
            k -= 1
            if i > 0:
                i -= 1
        num = num.lstrip('0')
        return num if num else '0'
# Runtime: 48 ms, faster than 75.15% of Python3 online submissions for Remove K Digits.
# Memory Usage: 14 MB, less than 16.00% of Python3 online submissions for Remove K Digits.
