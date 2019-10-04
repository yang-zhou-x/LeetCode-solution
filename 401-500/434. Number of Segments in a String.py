'''
Count the number of segments in a string, where a segment is defined to be a contiguous sequence of non-space characters.
Please note that the string does not contain any non-printable characters.

Example:
Input: "Hello, my name is John"
Output: 5
'''

class Solution:
    def countSegments(self, s: str) -> int:
        return len([x for x in s.split() if x])
# Runtime: 32 ms, faster than 88.54% of Python3 online submissions for Number of Segments in a String.
# Memory Usage: 13.6 MB, less than 6.67% of Python3 online submissions for Number of Segments in a String.

# space complexity: O(1)
class Solution:
    def countSegments(self, s: str) -> int:
        cnt = 0
        for i in range(len(s)):
            if s[i] != ' ' and (i == 0 or s[i-1] == ' '):
                cnt += 1
        return cnt
# Runtime: 36 ms, faster than 63.39% of Python3 online submissions for Number of Segments in a String.
# Memory Usage: 13.8 MB, less than 6.67% of Python3 online submissions for Number of Segments in a String.
