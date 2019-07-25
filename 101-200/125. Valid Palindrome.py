'''
Given a string, determine if it is a palindrome, 
considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:
Input: "A man, a plan, a canal: Panama"
Output: true

Example 2:
Input: "race a car"
Output: false
'''

class Solution:
    def isPalindrome(self, s: 'str') -> 'bool':
        s=''.join(filter(str.isalnum,s)).lower()
        return s==s[::-1]
# Runtime: 52 ms, faster than 97.56% of Python3 online submissions for Valid Palindrome.
# Memory Usage: 13.1 MB, less than 48.43% of Python3 online submissions for Valid Palindrome.

# 20190726
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 取出字母数字，并转成小写
        res = ''.join(filter(str.isalnum, s)).lower()
        return res == res[::-1]
# Runtime: 44 ms, faster than 93.44% of Python3 online submissions for Valid Palindrome.
# Memory Usage: 14.5 MB, less than 26.83% of Python3 online submissions for Valid Palindrome.
