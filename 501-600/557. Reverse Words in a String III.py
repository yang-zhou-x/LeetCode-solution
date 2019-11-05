'''
Given a string, you need to reverse the order of characters in each word within 
a sentence while still preserving whitespace and initial word order.

Example 1:
Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"

Note: 
In the string, each word is separated by single space and there will not be any extra space in the string.
'''

class Solution:
    def reverseWords(self, s: str) -> str:
        if not s:
            return s
        s_list = s.split()
        s_list = list(map(lambda x: ''.join(reversed(x)), s_list))
        return ' '.join(s_list)
# Runtime: 52 ms, faster than 31.40% of Python3 online submissions for Reverse Words in a String III.
# Memory Usage: 14.4 MB, less than 7.69% of Python3 online submissions for Reverse Words in a String III.
