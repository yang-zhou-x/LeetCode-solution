'''
Given a matrix of m x n elements (m rows, n columns), 
return all elements of the matrix in spiral order.

Example 1:
Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:
Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
'''

# 解法1: 每次一圈，逐个遍历。较慢
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        def get_idx(row_start, row_end, col_start, col_end):
            for c in range(col_start, col_end+1):  # 上侧
                yield row_start, c
            for r in range(row_start+1, row_end+1):  # 右侧
                yield r, col_end
            if row_start < row_end and col_start < col_end:
                for c in range(col_end-1, col_start, -1):  # 下侧
                    yield row_end, c
                for r in range(row_end, row_start, -1):  # 左侧
                    yield r, col_start

        if not matrix or not matrix[0]:
            return []
        r_s, r_e = 0, len(matrix)-1  # 索引
        c_s, c_e = 0, len(matrix[0])-1  # 索引
        ans = []
        while r_s <= r_e and c_s <= c_e:
            for r, c in get_idx(r_s, r_e, c_s, c_e):
                ans.append(matrix[r][c])
            r_s += 1
            r_e -= 1
            c_s += 1
            c_e -= 1
        return ans
# Runtime: 52 ms, faster than 9.11% of Python3 online submissions for Spiral Matrix.
# Memory Usage: 13 MB, less than 5.18% of Python3 online submissions for Spiral Matrix.

# 解法2: 思想与解法1相同，但是分为上右下左四段，非逐个
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        r_s, r_e = 0, len(matrix)-1  # 行索引
        c_s, c_e = 0, len(matrix[0])-1  # 列索引
        ans = []
        '''边界情况：
               head
              -------
         left |     |
              |     | right
              ------|
               tail
        '''
        flag = 'head'
        while r_s <= r_e and c_s <= c_e:
            if flag == 'head':
                ans += matrix[r_s][c_s:c_e+1]
                r_s += 1
                flag = 'right'
            elif flag == 'right':
                ans += [matrix[r][c_e] for r in range(r_s, r_e+1)]
                c_e -= 1
                flag = 'tail'
            elif flag == 'tail':
                sub = matrix[r_e][c_s:c_e+1]  # 在上一步中c_e已经-1，所以这里是+1
                sub.reverse()
                ans += sub
                r_e -= 1
                flag = 'left'
            elif flag == 'left':
                # 在上一步中r_e已经-1，所以这里不用-1
                # r_s在`head`步中+1，所以这里要-1
                ans += [matrix[r][c_s] for r in range(r_e, r_s-1, -1)]
                c_s += 1
                flag = 'head'
        return ans
# Runtime: 32 ms, faster than 96.16% of Python3 online submissions for Spiral Matrix.
# Memory Usage: 13.3 MB, less than 19.22% of Python3 online submissions for Spiral Matrix.
