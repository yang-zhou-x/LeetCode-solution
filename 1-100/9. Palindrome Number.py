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

# 转换为字符串进行处理
class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x)==str(x)[::-1]
# Runtime: 80 ms, faster than 97.64% of Python3 online submissions for Palindrome Number.
# Memory Usage: 13.1 MB, less than 5.03% of Python3 online submissions for Palindrome Number.
