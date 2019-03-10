class Solution:
    def isPalindrome(self, s: 'str') -> 'bool':
        s=''.join(filter(str.isalnum,s)).lower()
        return s==s[::-1]

# Runtime: 52 ms, faster than 97.56% of Python3 online submissions for Valid Palindrome.
# Memory Usage: 13.1 MB, less than 48.43% of Python3 online submissions for Valid Palindrome.
