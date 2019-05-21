'''
Given a non negative integer number num. 
For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's 
in their binary representation and return them as an array.

Example 1:
Input: 2
Output: [0,1,1]

Example 2:
Input: 5
Output: [0,1,1,2,1,2]

Follow up:
It is very easy to come up with a solution with run time O(n*sizeof(integer)). 
But can you do it in linear time O(n) /possibly in a single pass?
Space complexity should be O(n).
Can you do it like a boss? Do it without using any builtin function 
like __builtin_popcount in c++ or in any other language.
'''

class Solution:
    def countBits(self, num: int) -> List[int]:
        if num == 0:
            return [0]
        dp = [0]*(num+1)
        for i in range(1, num+1):
            dp[i] = dp[i >> 1]+i % 2  # i右移1位时的个数+末尾是否为1
        return dp
# Runtime: 112 ms, faster than 80.45% of Python3 online submissions for Counting Bits.
# Memory Usage: 15.9 MB, less than 44.50% of Python3 online submissions for Counting Bits.
