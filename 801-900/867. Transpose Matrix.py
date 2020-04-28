'''
Given a matrix A, return the transpose of A.
The transpose of a matrix is the matrix flipped over it's main diagonal, 
switching the row and column indices of the matrix.

Example 1:
Input: [[1,2,3],[4,5,6],[7,8,9]]
Output: [[1,4,7],[2,5,8],[3,6,9]]

Example 2:
Input: [[1,2,3],[4,5,6]]
Output: [[1,4],[2,5],[3,6]]
'''

class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        return [list(x) for x in zip(*A)]
# Runtime: 68 ms, faster than 94.50% of Python3 online submissions for Transpose Matrix.
# Memory Usage: 14.5 MB, less than 5.72% of Python3 online submissions for Transpose Matrix.
