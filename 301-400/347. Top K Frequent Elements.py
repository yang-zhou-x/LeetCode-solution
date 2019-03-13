class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        fre=collections.Counter(nums)
        
        return sorted(fre.keys(),key=fre.get,reverse=True)[:k]
        
# Runtime: 44 ms, faster than 99.34% of Python3 online submissions for Permutations.
