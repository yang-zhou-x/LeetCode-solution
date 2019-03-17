class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        aux=set()
        for n in nums:
            if n in aux:
                return n
            else:
                aux.add(n)
                
# Runtime: 40 ms, faster than 85.24% of Python3 online submissions for Find the Duplicate Number.
# Memory Usage: 15 MB, less than 7.85% of Python3 online submissions for Find the Duplicate Number.
