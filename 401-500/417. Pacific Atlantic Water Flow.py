'''
Given an m x n matrix of non-negative integers representing the height of each unit cell in a continent, 
the "Pacific ocean" touches the left and top edges of the matrix and 
the "Atlantic ocean" touches the right and bottom edges.
Water can only flow in four directions (up, down, left, or right) from a cell to another one with height equal or lower.
Find the list of grid coordinates where water can flow to both the Pacific and Atlantic ocean.

Note:
The order of returned grid coordinates does not matter.
Both m and n are less than 150.
 
Example:
Given the following 5x5 matrix:
  Pacific ~   ~   ~   ~   ~ 
       ~  1   2   2   3  (5) *
       ~  3   2   3  (4) (4) *
       ~  2   4  (5)  3   1  *
       ~ (6) (7)  1   4   5  *
       ~ (5)  1   1   2   4  *
          *   *   *   *   * Atlantic
Return:
[[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (positions with parentheses in above matrix).
'''

class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix or not matrix[0]:
            return []
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        m = len(matrix)
        n = len(matrix[0])
        p_visited = [[False for _ in range(n)] for _ in range(m)]
        a_visited = [[False for _ in range(n)] for _ in range(m)]
        result = []

        def dfs(i, j, visited):
            # when dfs called, meaning its caller already verified this point
            visited[i][j] = True
            for dir in directions:
                x, y = i + dir[0], j + dir[1]
                # 索引越界、已经流经过、流不到的情况
                if x < 0 or x >= m or y < 0 or y >= n \
                        or visited[x][y] or matrix[x][y] < matrix[i][j]:
                    continue
                dfs(x, y, visited)
        # 从海边流回格子。四条边都是True
        for i in range(m):
            # p_visited[i][0] = True
            # a_visited[i][n-1] = True
            dfs(i, 0, p_visited)
            dfs(i, n-1, a_visited)
        for j in range(n):
            # p_visited[0][j] = True
            # a_visited[m-1][j] = True
            dfs(0, j, p_visited)
            dfs(m-1, j, a_visited)

        for i in range(m):
            for j in range(n):
                if p_visited[i][j] and a_visited[i][j]:
                    result.append([i, j])
        return result
# Runtime: 328 ms, faster than 59.52% of Python3 online submissions for Pacific Atlantic Water Flow.
# Memory Usage: 15 MB, less than 5.41% of Python3 online submissions for Pacific Atlantic Water Flow.
