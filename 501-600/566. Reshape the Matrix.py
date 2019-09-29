'''
In MATLAB, there is a very useful function called 'reshape', which can reshape a 
matrix into a new one with different size but keep its original data.
You're given a matrix represented by a two-dimensional array, and two positive integers r 
and c representing the row number and column number of the wanted reshaped matrix, respectively.
The reshaped matrix need to be filled with all the elements of the original matrix in 
the same row-traversing order as they were.
If the 'reshape' operation with given parameters is possible and legal, 
output the new reshaped matrix; Otherwise, output the original matrix.

Example 1:
Input: 
nums = 
[[1,2],
 [3,4]]
r = 1, c = 4
Output: 
[[1,2,3,4]]
Explanation:
The row-traversing of nums is [1,2,3,4]. The new reshaped matrix is a 1 * 4 matrix, fill it row by row by using the previous list.

Example 2:
Input: 
nums = 
[[1,2],
 [3,4]]
r = 2, c = 4
Output: 
[[1,2],
 [3,4]]
Explanation:
There is no way to reshape a 2 * 2 matrix to a 2 * 4 matrix. So output the original matrix.

Note:
The height and width of the given matrix is in range [1, 100].
The given r and c are all positive.
'''

class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        if not nums or not nums[0]:
            return nums
        m = len(nums)
        n = len(nums[0])
        if m * n != r * c:
            return nums
        new = [[0] * c for _ in range(r)]
        row, col = 0, 0
        for line in nums:
            for n in line:
                new[row][col] = n
                col += 1
                if col == c:
                    row += 1
                    col = 0
        return new
# Runtime: 112 ms, faster than 91.93% of Python3 online submissions for Reshape the Matrix.
# Memory Usage: 14.8 MB, less than 5.55% of Python3 online submissions for Reshape the Matrix.
