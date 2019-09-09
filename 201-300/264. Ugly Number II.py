'''
Write a program to find the n-th ugly number.
Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 

Example:
Input: n = 10
Output: 12
Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.

Note:  
1 is typically treated as an ugly number.
n does not exceed 1690.
'''

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [1] * n
        idx2, idx3, idx5 = 0, 0, 0
        left = 1
        while n > 1:
            t2, t3, t5 = 2 * dp[idx2], 3 * dp[idx3], 5 * dp[idx5]
            tmp = min(t2, t3, t5)
            if tmp == t2:
                idx2 += 1
            elif tmp == t3:
                idx3 += 1
            else:
                idx5 += 1
            if tmp != dp[left-1]:  # 不重复时
                dp[left] = tmp
                left += 1
                n -= 1
        return dp[-1]
# Runtime: 268 ms, faster than 22.50% of Python3 online submissions for Ugly Number II.
# Memory Usage: 14 MB, less than 20.00% of Python3 online submissions for Ugly Number II.
