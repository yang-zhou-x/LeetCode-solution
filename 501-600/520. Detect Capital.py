'''
Given a word, you need to judge whether the usage of capitals in it is right or not.
We define the usage of capitals in a word to be right when one of the following cases holds:
All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital, like "Google".

Otherwise, we define that this word doesn't use capitals in a right way.

Example 1:
Input: "USA"
Output: True

Example 2:
Input: "FlaG"
Output: False

Note: The input will be a non-empty word consisting of uppercase and lowercase latin letters.
'''

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word) < 2:
            return True
        cap_first = ord(word[0]) < ord('a')
        cap_rest = sum(map(lambda x: ord(x) < ord('a'), word[1:]))
        if cap_first and (cap_rest == 0 or cap_rest + 1 == len(word)):
            return True
        elif not cap_first and cap_rest == 0:
            return True
        else:
            return False
# Runtime: 40 ms, faster than 42.42% of Python3 online submissions for Detect Capital.
# Memory Usage: 13.8 MB, less than 6.67% of Python3 online submissions for Detect Capital.
