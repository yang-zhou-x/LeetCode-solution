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
        
        def back_track(idx, path):
            if idx == len(digits):
                ans.append(path)
            else:
                for cha in phone[digits[idx]]:
                    back_track(idx + 1, path + cha)
        if digits:
            back_track(0, '')
        return ans
# Runtime: 32 ms, faster than 90.34% of Python3 online submissions for Letter Combinations of a Phone Number.
# Memory Usage: 14.1 MB, less than 5.23% of Python3 online submissions for Letter Combinations of a Phone Number.
