'''
Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
Find all the elements that appear twice in this array.
Could you do it without extra space and in O(n) runtime?

Example:
Input:
[4,3,2,7,8,2,3,1]
Output:
[2,3]
'''

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        for n in nums:
            if nums[abs(n) - 1] < 0:
                ans.append(abs(n))
            else:
                nums[abs(n) - 1] *= -1
        return ans
# Runtime: 428 ms, faster than 55.72% of Python3 online submissions for Find All Duplicates in an Array.
# Memory Usage: 21.6 MB, less than 7.14% of Python3 online submissions for Find All Duplicates in an Array.
