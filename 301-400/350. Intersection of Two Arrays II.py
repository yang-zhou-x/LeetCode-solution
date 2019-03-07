class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        aux=collections.Counter(nums1)
        ans=[]
        for n in nums2:
            if aux.get(n):
                ans.append(n)
                aux[n]-=1
        return ans
        
# Runtime: 24 ms, faster than 94.23% of Python online submissions for Intersection of Two Arrays II.
# Memory Usage: 10.9 MB, less than 35.91% of Python online submissions for Intersection of Two Arrays II.
 
