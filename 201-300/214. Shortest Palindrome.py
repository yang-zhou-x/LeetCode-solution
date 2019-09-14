'''
Given a string s, you are allowed to convert it to a palindrome by adding characters in front of it. Find and return the shortest palindrome you can find by performing this transformation.

Example 1:
Input: "aacecaaa"
Output: "aaacecaaa"

Example 2:
Input: "abcd"
Output: "dcbabcd"
'''

class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s
        
        def expand(left, right):
            if left == right:
                if s[:left+1] == s[left:left+left+1][::-1]:
                    return left
                else:
                    return float('-inf')
            else:
                if s[:left+1] == s[right:right+right][::-1]:
                    return right
                else:
                    return float('-inf')

        center, interval = float('-inf'), False
        for i in range((len(s) + 1) // 2 - 1, -1, -1):  # 数字为中心
            tmp = expand(i, i)
            if tmp > center:
                center = tmp
                break
        for i in range((len(s) + 1) // 2, 0, -1):  # 间隔为中心
            tmp = expand(i-1, i)
            if tmp > center:
                interval = True
                center = tmp
                break
        
        if interval:
            return s[center * 2:][::-1] + s
        else:
            return s[center * 2 + 1:][::-1] + s
# Runtime: 300 ms, faster than 30.49% of Python3 online submissions for Shortest Palindrome.
# Memory Usage: 14.1 MB, less than 14.29% of Python3 online submissions for Shortest Palindrome.
