'''
Given a string containing digits from 2-9 inclusive, 
return all possible letter combinations that the number could represent.
A mapping of digit to letters (just like on the telephone buttons) is given below. 
Note that 1 does not map to any letters.

Example:
Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

Note:
Although the above answer is in lexicographical order, your answer could be in any order you want.
'''

class Solution:
    def letterCombinations(self, digits: 'str') -> 'List[str]':
        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}
        ans=[]
        def backTrack(comb,digit):
            if len(digit)==0:
                ans.append(comb)
            else:
                for letter in phone[digit[0]]:
                    backTrack(comb+letter,digit[1:])
        if digits:
            backTrack('',digits)
        return ans
# Runtime: 36 ms, faster than 71.05% of Python3 online submissions for Letter Combinations of a Phone Number.
# Memory Usage: 13.1 MB, less than 5.86% of Python3 online submissions for Letter Combinations of a Phone Number.

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}
        ans = []
        def helper(path, idx):
            if idx == len(digits):
                ans.append(path)
            else:
                for p in phone[digits[idx]]:
                    helper(path + p, idx + 1)
        if digits:
            helper('', 0)
        return ans
# Runtime: 32 ms, faster than 90.34% of Python3 online submissions for Letter Combinations of a Phone Number.
# Memory Usage: 14.1 MB, less than 5.23% of Python3 online submissions for Letter Combinations of a Phone Number.
