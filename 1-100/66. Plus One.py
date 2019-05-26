'''
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.
The digits are stored such that the most significant digit is at the head of the list, 
and each element in the array contain a single digit.
You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:
Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.

Example 2:
Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
'''

# 解法1
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits[-1]+=1
        if digits[-1]<10:
            return digits
        next_=0
        for i in range(len(digits)-1,-1,-1):
            next_,digits[i]=divmod(digits[i]+next_,10)
        if next_!=0:
            digits.insert(0,1)
        return digits
# Runtime: 20 ms, faster than 97.80% of Python online submissions for Plus One.
# Memory Usage: 10.8 MB, less than 18.79% of Python online submissions for Plus One.

# 解法2
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        right = len(digits)-1
        while digits[right] == 9:
            digits[right] = 0
            right -= 1
        if right < 0:  # 全部为9时
            digits.insert(0, 1)
            return digits
        digits[right] += 1  # 当前位置+1
        return digits
# Runtime: 32 ms, faster than 98.17% of Python3 online submissions for Plus One.
# Memory Usage: 13 MB, less than 76.41% of Python3 online submissions for Plus One.
