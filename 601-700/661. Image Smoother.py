'''
Given a 2D integer matrix M representing the gray scale of an image, 
you need to design a smoother to make the gray scale of each cell becomes 
the average gray scale (rounding down) of all the 8 surrounding cells and itself. 
If a cell has less than 8 surrounding cells, then use as many as you can.

Example 1:
Input:
[[1,1,1],
 [1,0,1],
 [1,1,1]]
Output:
[[0, 0, 0],
 [0, 0, 0],
 [0, 0, 0]]
Explanation:
For the point (0,0), (0,2), (2,0), (2,2): floor(3/4) = floor(0.75) = 0
For the point (0,1), (1,0), (1,2), (2,1): floor(5/6) = floor(0.83333333) = 0
For the point (1,1): floor(8/9) = floor(0.88888889) = 0

Note:
The value in the given matrix is in the range of [0, 255].
The length and width of the given matrix are in the range of [1, 150].
'''

class Solution:
    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:

        def cal(x, y):
            directions = (-1, 0, 1)
            tot, cnt = 0, 0
            for i in directions:
                for j in directions:
                    tmp_x = x + i
                    tmp_y = y + j
                    if tmp_x < 0 or tmp_x >= len(M) or \
                            tmp_y < 0 or tmp_y >= len(M[0]):
                        pass
                    else:
                        tot += M[tmp_x][tmp_y]
                        cnt += 1
            return int(tot / cnt)

        ans = [[0] * len(M[0]) for _ in range(len(M))]
        for i in range(len(M)):
            for j in range(len(M[0])):
                ans[i][j] = cal(i, j)
        return ans
# Runtime: 772 ms, faster than 47.94% of Python3 online submissions for Image Smoother.
# Memory Usage: 13.1 MB, less than 100.00% of Python3 online submissions for Image Smoother.
