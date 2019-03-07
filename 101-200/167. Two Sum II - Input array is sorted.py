class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        aux={}
        for i,n in enumerate(numbers,1):
            if target-n in aux:
                return [aux[target-n],i]
            aux[n]=i
        
# Runtime: 16 ms, faster than 100.00% of Python online submissions for Two Sum II - Input array is sorted.
# Memory Usage: 10.9 MB, less than 53.75% of Python online submissions for Two Sum II - Input array is sorted.

