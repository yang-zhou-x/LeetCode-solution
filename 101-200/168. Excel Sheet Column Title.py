'''
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:
    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
    ...

Example 1:
Input: 1
Output: "A"

Example 2:
Input: 28
Output: "AB"

Example 3:
Input: 701
Output: "ZY"
'''

class Solution:
    def convertToTitle(self, n: int) -> str:
        letters = [chr(x) for x in range(65, 91)]
        mapping = {x:y for x, y in zip(range(1, 27), letters)}
        if n < 27:
            return mapping[n]
        ans = ''
        while n > 26:
            n, remain = divmod(n, 26)
            if remain == 0:
                remain = 26
                n -= 1
            ans = mapping[remain] + ans
        return mapping[n] + ans
# Runtime: 32 ms, faster than 88.12% of Python3 online submissions for Excel Sheet Column Title.
# Memory Usage: 13.9 MB, less than 6.25% of Python3 online submissions for Excel Sheet Column Title.
