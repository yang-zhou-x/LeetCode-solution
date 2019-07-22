'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: 
(you may want to display this pattern in a fixed font for better legibility)
P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:
string convert(string s, int numRows);

Example 1:
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

Example 2:
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
'''

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if not s:
            return s
        if numRows == 0 or numRows == 1:
            return s
        n = len(s)
        cycle = 2 * numRows - 2
        ans = ''
        for i in range(numRows):
            for j in range(i, n, cycle):
                ans += s[j]
                # 非首行尾行时
                if i != 0 and i != numRows - 1 and j + cycle - 2 * i < n:
                    ans += s[j + cycle - 2 * i]
        return ans
# Runtime: 64 ms, faster than 78.53% of Python3 online submissions for ZigZag Conversion.
# Memory Usage: 13.9 MB, less than 6.89% of Python3 online submissions for ZigZag Conversion.
