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

# 改进方法
# 1）先计数，从字符数量上判断是否存在可能
# 2）去掉list的slice操作
