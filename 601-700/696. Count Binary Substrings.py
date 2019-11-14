'''
Give a string s, count the number of non-empty (contiguous) substrings that have the same number of 0's 
and 1's, and all the 0's and all the 1's in these substrings are grouped consecutively.
Substrings that occur multiple times are counted the number of times they occur.

Example 1:
Input: "00110011"
Output: 6
Explanation: There are 6 substrings that have equal number of consecutive 1's and 0's: 
"0011", "01", "1100", "10", "0011", and "01".
Notice that some of these substrings repeat and are counted the number of times they occur.
Also, "00110011" is not a valid substring because all the 0's (and 1's) are not grouped together.

Example 2:
Input: "10101"
Output: 4
Explanation: There are 4 substrings: "10", "01", "10", "01" that have equal number of consecutive 1's and 0's.

Note:
s.length will be between 1 and 50,000.
s will only consist of "0" or "1" characters.
'''

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        if len(s) < 2:
            return 0
        groups = [1]
        for i in range(1, len(s)):
            if s[i-1] != s[i]:
                groups.append(1)
            else:
                groups[-1] += 1
        ans = 0
        for i in range(1, len(groups)):
            ans += min(groups[i-1], groups[i])
        return ans
# Runtime: 208 ms, faster than 41.67% of Python3 online submissions for Count Binary Substrings.
# Memory Usage: 13.2 MB, less than 75.00% of Python3 online submissions for Count Binary Substrings.

from itertools import groupby
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        if len(s) < 2:
            return 0
        groups = [len(list(cnt)) for _, cnt in groupby(s)]
        return sum(min(a, b) for a, b in zip(groups, groups[1:]))
# Runtime: 172 ms, faster than 66.37% of Python3 online submissions for Count Binary Substrings.
# Memory Usage: 13.4 MB, less than 33.33% of Python3 online submissions for Count Binary Substrings.


# 空间复杂度更低的方法
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        if len(s) < 2:
            return 0
        ans = 0
        prev, curr = 0, 1
        for i in range(1, len(s)):
            if s[i-1] == s[i]:
                curr += 1
            else:
                ans += min(prev, curr)
                prev = curr
                curr = 1
        return ans + min(prev, curr)
# Runtime: 160 ms, faster than 78.36% of Python3 online submissions for Count Binary Substrings.
# Memory Usage: 13.1 MB, less than 100.00% of Python3 online submissions for Count Binary Substrings.
