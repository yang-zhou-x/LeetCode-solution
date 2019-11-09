'''
Given a non-empty string s, you may delete at most one character. 
Judge whether you can make it a palindrome.

Example 1:
Input: "aba"
Output: True

Example 2:
Input: "abca"
Output: True
Explanation: You could delete the character 'c'.

Note:
The string will only contain lowercase characters a-z. 
The maximum length of the string is 50000.
'''

class Solution:
    def validPalindrome(self, s: str) -> bool:
        self.del_cnt = 0
        left, right = 0, len(s) - 1
        
        def check(left, right):
            while left < right:
                if s[left] != s[right]:
                    self.del_cnt += 1
                    if self.del_cnt > 1:
                        return False
                    if s[left] == s[right-1] and s[left+1] == s[right]:
                        return check(left, right-1) or check(left+1, right)
                    elif s[left] == s[right-1]:
                        return check(left, right-1)
                    elif s[left+1] == s[right]:
                        return check(left+1, right)
                    else:
                        return False
                else:
                    left += 1
                    right -= 1
            return True
        
        return check(left, right)
# Runtime: 176 ms, faster than 48.47% of Python3 online submissions for Valid Palindrome II.
# Memory Usage: 15.6 MB, less than 6.25% of Python3 online submissions for Valid Palindrome II.

# 没啥区别的另一种写法
class Solution:
    def validPalindrome(self, s: str) -> bool:
        del_cnt = 0
        left, right = 0, len(s) - 1
        
        def check(left, right):
            while left < right:
                if s[left] != s[right]:
                    nonlocal del_cnt
                    del_cnt += 1
                    if del_cnt > 1:
                        return False
                    if s[left] == s[right-1] and s[left+1] == s[right]:
                        return check(left, right-1) or check(left+1, right)
                    elif s[left] == s[right-1]:
                        return check(left, right-1)
                    elif s[left+1] == s[right]:
                        return check(left+1, right)
                    else:
                        return False
                else:
                    left += 1
                    right -= 1
            return True
        
        return check(left, right)
# Runtime: 172 ms, faster than 52.65% of Python3 online submissions for Valid Palindrome II.
# Memory Usage: 14.9 MB, less than 6.25% of Python3 online submissions for Valid Palindrome II.
