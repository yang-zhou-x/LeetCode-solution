'''
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

Note: The algorithm should run in linear time and in O(1) space.

Example 1:
Input: [3,2,3]
Output: [3]

Example 2:
Input: [1,1,1,3,3,2,2,2]
Output: [1,2]
'''

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        candi1, candi2 = 0, 1  # 随机的两个数
        cnt1, cnt2 = 0, 0
        for n in nums:
            if n == candi1:
                cnt1 += 1
            elif n == candi2:
                cnt2 += 1
            elif cnt1 == 0:
                candi1 = n
                cnt1 = 1
            elif cnt2 == 0:
                candi2 = n
                cnt2 = 1
            else:
                cnt1 -= 1
                cnt2 -= 1
        return [x for x in (candi1,candi2) if len(nums)/3 < nums.count(x)]
# Runtime: 136 ms, faster than 75.42% of Python3 online submissions for Majority Element II.
# Memory Usage: 15.1 MB, less than 5.88% of Python3 online submissions for Majority Element II.
