class Solution:
    def increasingTriplet(self, nums: 'List[int]') -> 'bool':
        a,b=float('inf'),float('inf')
        for n in nums:
            if n<=a:
                a=n  # a最小
            elif n<=b:
                b=n  # b中间
            else:  # 存在比b大的数字
                return True
        return False
        
# Runtime: 36 ms, faster than 98.53% of Python3 online submissions for Increasing Triplet Subsequence.
# Memory Usage: 13.5 MB, less than 6.80% of Python3 online submissions for Increasing Triplet Subsequence.
