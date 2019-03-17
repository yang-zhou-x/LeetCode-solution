class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return heapq.nlargest(k,nums)[-1]
        
# Runtime: 36 ms, faster than 99.59% of Python3 online submissions for Kth Largest Element in an Array.
