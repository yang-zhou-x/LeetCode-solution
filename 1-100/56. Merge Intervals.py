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
