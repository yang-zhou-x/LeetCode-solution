'''
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).
You may assume that the intervals were initially sorted according to their start times.

Example 1:
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Example 2:
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

NOTE: 
input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.
'''

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]):
        if not intervals:
            return [newInterval]
        ans = []
        left = 0
        while left < len(intervals):
            if newInterval[0] <= intervals[left][1]:
                break
            left += 1
        ans += intervals[:left]
        # 注意边界
        if left == len(intervals) or newInterval[1] < intervals[left][0]:
            ans.append(newInterval)
            ans += intervals[left:]
            return ans

        new_s = newInterval[0] if newInterval[0] < intervals[left][0] \
            else intervals[left][0]
        while left < len(intervals) and newInterval[1] >= intervals[left][1]:
            left += 1
        # 注意边界
        if left == len(intervals) or newInterval[1] < intervals[left][0]:
            ans.append([new_s, newInterval[1]])
            ans += intervals[left:]
        else:
            ans.append([new_s, intervals[left][1]])
            ans += intervals[left+1:]
        return ans
# Runtime: 84 ms, faster than 97.87% of Python3 online submissions for Insert Interval.
# Memory Usage: 17.2 MB, less than 8.00% of Python3 online submissions for Insert Interval.
