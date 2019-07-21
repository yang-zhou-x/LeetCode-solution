'''
Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.
Note that the row index starts from 0.
In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:
Input: 3
Output: [1,3,3,1]

Follow up:
Could you optimize your algorithm to use only O(k) extra space?
'''

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1, 1]
        ans = [1] * (rowIndex + 1)
        last_row = self.getRow(rowIndex - 1)
        for i in range(1, rowIndex):
            ans[i] = last_row[i - 1] + last_row[i]
        return ans
# Runtime: 32 ms, faster than 91.21% of Python3 online submissions for Pascal's Triangle II.
# Memory Usage: 13.8 MB, less than 5.08% of Python3 online submissions for Pascal's Triangle II.
