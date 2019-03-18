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
