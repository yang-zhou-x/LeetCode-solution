'''
Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.

Note:
The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000
'''

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxi, tmp = 0, 0
        for n in nums:
            if n == 0:
                if tmp > maxi:
                    maxi = tmp
                tmp = 0
            else:
                tmp += 1
        return maxi if maxi > tmp else tmp
# Runtime: 396 ms, faster than 91.63% of Python3 online submissions for Max Consecutive Ones.
# Memory Usage: 14.2 MB, less than 7.69% of Python3 online submissions for Max Consecutive Ones.
