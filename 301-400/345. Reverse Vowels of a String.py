'''
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:
Input: "hello"
Output: "holle"

Example 2:
Input: "leetcode"
Output: "leotcede"
Note:
The vowels does not include the letter "y".
'''

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {'a', 'e', 'i', 'o', 'u',
                  'A', 'E', 'I', 'O', 'U'}
        s = list(s)
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] in vowels and s[right] in vowels:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
            elif s[left] in vowels:
                right -= 1
            elif s[right] in vowels:
                left += 1
            else:
                left += 1
                right -= 1
        return ''.join(s)
# Runtime: 56 ms, faster than 85.86% of Python3 online submissions for Reverse Vowels of a String.
# Memory Usage: 14.8 MB, less than 14.87% of Python3 online submissions for Reverse Vowels of a String.
