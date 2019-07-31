'''
Given an encoded string, return its decoded string.
The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets 
is being repeated exactly k times. Note that k is guaranteed to be a positive integer.
You may assume that the input string is always valid; 
No extra white spaces, square brackets are well-formed, etc.
Furthermore, you may assume that the original data does not contain any digits 
and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

Examples:
s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
'''

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []        
        for ch in s:
            if ch == ']':
                tmp = ''  # substring needing to be repeated
                while stack[-1] != '[':
                    tmp = stack.pop() + tmp
                stack.pop()
                n = ''  # number of repetitions of the substring
                while stack and stack[-1].isdigit():
                    n = stack.pop() + n
                stack.append(tmp * int(n))  # put it in stack
            else:
                stack.append(ch)
        return ''.join(stack)
# Runtime: 36 ms, faster than 64.31% of Python3 online submissions for Decode String.
# Memory Usage: 13.9 MB, less than 5.36% of Python3 online submissions for Decode String.
