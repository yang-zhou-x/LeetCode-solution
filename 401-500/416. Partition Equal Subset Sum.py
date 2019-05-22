'''
Given a non-empty array containing only positive integers, 
find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

Note:
Each of the array element will not exceed 100.
The array size will not exceed 200.
 
Example 1:
Input: [1, 5, 11, 5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
 
Example 2:
Input: [1, 2, 3, 5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.
'''

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        tot = sum(nums)
        if tot % 2:  # 和为奇数时，必定False
            return False
        half = tot >> 1
        cache = {0}  # 保存小于half的所有和
        for n in sorted(nums, reverse=True):  # 从大到小排序，加速
            if n > half:
                break
            for c in cache.copy():
                tmp = n+c
                if tmp == half:
                    return True
                elif tmp < half:
                    cache.add(tmp)
        return False
# Runtime: 188 ms, faster than 72.66% of Python3 online submissions for Partition Equal Subset Sum.
# Memory Usage: 13.6 MB, less than 40.41% of Python3 online submissions for Partition Equal Subset Sum.
