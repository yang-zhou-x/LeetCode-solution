'''
Given an array of size n, find the majority element. 
The majority element is the element that appears more than ⌊ n/2 ⌋ times.
You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:
Input: [3,2,3]
Output: 3

Example 2:
Input: [2,2,1,1,1,2,2]
Output: 2
'''

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        for n in nums:
            if count == 0:
                ans = n
            count += 1 if n == ans else -1
        return ans
# Runtime: 44 ms, faster than 97.06% of Python3 online submissions for Majority Element.
# Memory Usage: 14.3 MB, less than 69.85% of Python3 online submissions for Majority Element.

# easy understanding
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        for n in nums:
            if count == 0:
                num = n
                count = 1
            elif n == num:
                count += 1
            else:
                count -= 1
        return num
# Runtime: 188 ms, faster than 91.81% of Python3 online submissions for Majority Element.
# Memory Usage: 15.1 MB, less than 7.14% of Python3 online submissions for Majority Element.
