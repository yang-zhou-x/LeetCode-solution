'''
Given a collection of intervals, merge all overlapping intervals.

Example 1:
Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Example 2:
Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

NOTE: 
input types have been changed on April 15, 2019. 
Please reset to default code definition to get new method signature.
'''

# April 15, 2019之前的旧版本：
# 
# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals: List[Interval]) -> List[Interval]:
        intervals.sort(key=lambda x:x.start) # 先排序
        ans=[]
        for i in intervals:
            if not ans or ans[-1].end<i.start: # ans为空，或者最后一个interval的end小于新的start时，往ans中添加一个
                ans.append(i)
            else: # 合并interval
                ans[-1].end=max(ans[-1].end,i.end)
        return ans
# Runtime: 56 ms, faster than 98.18% of Python3 online submissions for Merge Intervals.
# Memory Usage: 15.7 MB, less than 5.34% of Python3 online submissions for Merge Intervals.

# April 15, 2019之后的新版本：
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort(key=lambda x: x[0])  # 先排序
        ans = []
        for i in intervals:
             # ans为空，或者最后一个interval的end小于新的start时，往ans中添加一个
            if not ans or ans[-1][-1] < i[0]:
                ans.append(i)
            else:  # 合并interval
                ans[-1][-1] = max(ans[-1][-1], i[-1])
        return ans
# Runtime: 44 ms, faster than 98.53% of Python3 online submissions for Merge Intervals.
# Memory Usage: 14.1 MB, less than 98.56% of Python3 online submissions for Merge Intervals.

