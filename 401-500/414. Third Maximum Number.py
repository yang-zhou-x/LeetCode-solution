'''
Given a non-empty array of integers, return the third maximum number in this array.
If it does not exist, return the maximum number. The time complexity must be in O(n).

Example 1:
Input: [3, 2, 1]
Output: 1
Explanation: The third maximum is 1.

Example 2:
Input: [1, 2]
Output: 2
Explanation: The third maximum does not exist, so the maximum (2) is returned instead.

Example 3:
Input: [2, 2, 3, 1]
Output: 1

Explanation: Note that the third maximum here means the third maximum distinct number.
Both numbers with value 2 are both considered as second maximum.
'''

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        fir = sec = thi = float('-inf')
        visited = set()
        for n in nums:
            if n in visited:
                continue
            elif n > fir:
                fir, sec, thi = n, fir, sec
            elif n > sec:
                sec, thi = n, sec
            elif n > thi:
                thi = n
            else:
                continue
            visited.add(n)
        return thi if thi != float('-inf') else fir
# Runtime: 60 ms, faster than 85.21% of Python3 online submissions for Third Maximum Number.
# Memory Usage: 14.6 MB, less than 7.69% of Python3 online submissions for Third Maximum Number.
