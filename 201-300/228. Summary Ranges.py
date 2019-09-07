'''
Given a sorted integer array without duplicates, return the summary of its ranges.

Example 1:
Input:  [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: 0,1,2 form a continuous range; 4,5 form a continuous range.

Example 2:
Input:  [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: 2,3,4 form a continuous range; 8,9 form a continuous range.
'''

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        left = right = nums[0]
        ans = []
        for i in range(1, len(nums)):
            if nums[i] - 1 == right:
                right += 1
            else:
                if left == right:
                    ans.append(str(left))
                else:
                    ans.append(str(left) + '->' + str(right))
                left = right = nums[i]
        if left == right:
            ans.append(str(left))
        else:
            ans.append(str(left) + '->' + str(right))
        return ans
# Runtime: 40 ms, faster than 27.54% of Python3 online submissions for Summary Ranges.
# Memory Usage: 13.9 MB, less than 16.67% of Python3 online submissions for Summary Ranges.
