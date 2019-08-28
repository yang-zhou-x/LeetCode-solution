'''
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:
Input: 121
Output: true

Example 2:
Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:
Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Follow up:
Coud you solve it without converting the integer to a string?
'''

# 转换为字符串进行处理
class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x)==str(x)[::-1]
# Runtime: 80 ms, faster than 97.64% of Python3 online submissions for Palindrome Number.
# Memory Usage: 13.1 MB, less than 5.03% of Python3 online submissions for Palindrome Number.

# 不转换为字符串
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        raw=x
        ans=0
        while raw>0:
            raw,remainder=divmod(raw,10)
            ans=ans*10+remainder
        if ans==x:
            return True
        else:
            return False
# Runtime: 96 ms, faster than 90.63% of Python3 online submissions for Palindrome Number.
# Memory Usage: 13.2 MB, less than 5.03% of Python3 online submissions for Palindrome Number.

# 20190828更新
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        old = x
        new = 0
        while x:
            x, remainder = divmod(x, 10)
            new = new * 10 + remainder
        return old == new
# Runtime: 72 ms, faster than 61.76% of Python3 online submissions for Palindrome Number.
# Memory Usage: 14.1 MB, less than 6.50% of Python3 online submissions for Palindrome Number.

