class Solution:
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.origin=nums        

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.origin

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """   
        return sorted(self.origin,key=lambda x:random.random())

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()

# Runtime: 356 ms, faster than 94.75% of Python3 online submissions for Shuffle an Array.
# Memory Usage: 19.1 MB, less than 5.80% of Python3 online submissions for Shuffle an Array.
