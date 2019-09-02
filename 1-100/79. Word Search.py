'''
Given a 2D board and a word, find if the word exists in the grid.
The word can be constructed from letters of sequentially adjacent cell, 
where "adjacent" cells are those horizontally or vertically neighboring. 
The same letter cell may not be used more than once.

Example:
board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
'''

# 解法1
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board:
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, i, j, word): # 每个位置都作为起点搜索该词
                    return True
        return False

    # 检查从(i,j)位置开始是否可以找到word  
    def dfs(self, board, i, j, word):
        if len(word) == 0: # 所有位置都被检查过
            return True
        if i<0 or i>=len(board) or j<0 or j>=len(board[0]) or board[i][j]!=word[0]:
            return False # 索引越界或者当前位置不等于首字母
        tmp = board[i][j]  # 第1个字母符合条件，检查剩余的字母
        board[i][j] = '-'  # 每个字母只能使用一次。避免重复使用。
        # 检查是否可以延某个方向找到剩余字母
        res = self.dfs(board, i+1, j, word[1:]) or self.dfs(board, i-1, j, word[1:]) or self.dfs(board, i, j+1, word[1:]) or self.dfs(board, i, j-1, word[1:])
        board[i][j] = tmp # 改回
        return res
# Runtime: 296 ms, faster than 39.95% of Python3 online submissions for Word Search.
# Memory Usage: 14.4 MB, less than 20.41% of Python3 online submissions for Word Search.

# 解法2：改进方法
# 1）先计数，从字符数量上判断是否存在可能
# 2）去掉list的slice操作，改用索引
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not board[0] or not word:
            return False
        # 字符计数
        count = collections.Counter(c for row in board for c in row)
        # 从字符类别和数量上先判断一下
        for c, cnt in collections.Counter(word).items():
            if c not in count or cnt > count[c]:
                return False

        def dfs(i, x, y):  # 从board[x][y]开始，寻找周围是否有word[i]
            if i >= len(word):  # 终止
                return True
            c = board[x][y]
            board[x][y] = ''  # 不能重复使用，先用空字符占位
            # 向上、下、左、右4个方向寻找
            if x > 0 and board[x - 1][y] == word[i] and dfs(i + 1, x - 1, y):
                return True
            if x + 1 < m and board[x + 1][y] == word[i] and dfs(i + 1, x + 1, y):
                return True
            if y > 0 and board[x][y - 1] == word[i] and dfs(i + 1, x, y - 1):
                return True
            if y + 1 < n and board[x][y + 1] == word[i] and dfs(i + 1, x, y + 1):
                return True
            board[x][y] = c  # 复原
            return False
        m, n = len(board), len(board[0])
        # 从每个等于word[0]的位置开始。只要存在1个True，返回True
        return any(dfs(1, x, y) for x in range(m) for y in range(n) if board[x][y] == word[0])
# Runtime: 48 ms, faster than 100.00% of Python3 online submissions for Word Search.
# Memory Usage: 14.3 MB, less than 59.77% of Python3 online submissions for Word Search.


# 20190902，思路不变，略有改动
from collections import Counter

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not board[0]:
            return False
        # 先从字母及其数量判断
        board_cnt = Counter(x for line in board for x in line)
        word_cnt = Counter(word)
        for key in word_cnt:
            if key not in board_cnt or word_cnt[key] > board_cnt[key]:
                return False
        
        def back_track(idx, x, y):
            if board[x][y] != word[idx]:
                return False
            if idx + 1 == len(word):
                return True
            curr = board[x][y]
            board[x][y] = '*'  # 不能重复使用，占位
            if x > 0 and back_track(idx + 1, x - 1, y):  # 向上
                return True
            if x + 1 < len(board) and back_track(idx + 1, x + 1, y):  # 向下
                return True
            if y > 0 and back_track(idx + 1, x, y - 1):  # 向左
                return True
            if y + 1 < len(board[0]) and back_track(idx + 1, x, y + 1):  # 向右
                return True
            board[x][y] = curr  # 复原
            return False

        return any(back_track(0, i, j) \
                   for i in range(len(board)) \
                   for j in range(len(board[0])))
# Runtime: 172 ms, faster than 99.33% of Python3 online submissions for Word Search.
# Memory Usage: 15.3 MB, less than 17.02% of Python3 online submissions for Word Search.
