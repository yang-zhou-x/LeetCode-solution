'''
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
Find all the elements of [1, n] inclusive that do not appear in this array.
Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:
Input:
[4,3,2,7,8,2,3,1]
Output:
[5,6]
'''

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        cache = set(nums)
        return [x for x in range(1, len(nums)+1) if x not in cache]
# Runtime: 128 ms, faster than 99.51% of Python3 online submissions for Find All Numbers Disappeared in an Array.
# Memory Usage: 20.9 MB, less than 31.33% of Python3 online submissions for Find All Numbers Disappeared in an Array.
