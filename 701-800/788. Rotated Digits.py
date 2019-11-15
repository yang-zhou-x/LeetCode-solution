'''
X is a good number if after rotating each digit individually by 180 degrees, 
we get a valid number that is different from X.  Each digit must be rotated - we cannot choose to leave it alone.
A number is valid if each digit remains a digit after rotation. 0, 1, 
and 8 rotate to themselves; 2 and 5 rotate to each other; 6 and 9 rotate to each other, 
and the rest of the numbers do not rotate to any other number and become invalid.
Now given a positive number N, how many numbers X from 1 to N are good?

Example:
Input: 10
Output: 4
Explanation: 
There are four good numbers in the range [1, 10] : 2, 5, 6, 9.
Note that 1 and 10 are not good numbers, since they remain unchanged after rotating.

Note:
N  will be in range [1, 10000].
'''

class Solution:
    def rotatedDigits(self, N: int) -> int:
        mapping = {'0': '0', '1': '1', '8': '8',
                   '2': '5', '5': '2', '6': '9', '9': '6'}
        ans = 0
        for i in range(1, N + 1):
            curr = str(i)
            new = ''
            for cha in curr:
                tmp = mapping.get(cha, None)
                if tmp:
                    new += tmp
                else:
                    break
            if len(curr) == len(new) and curr != new:
                ans += 1
        return ans
# Runtime: 100 ms, faster than 62.01% of Python3 online submissions for Rotated Digits.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Rotated Digits.
