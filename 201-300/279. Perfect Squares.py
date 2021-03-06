'''
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:
Input: n = 12
Output: 3 
Explanation: 12 = 4 + 4 + 4.

Example 2:
Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
'''

# BFS算法
class Solution:
    def numSquares(self, n: int) -> int:
        # n=0,1时：
        if n<2:
            return n
        # n>=2时：
        i=1
        square=[]
        while i**2<=n:
            square.append(i**2)  # 存放小于n的平方数
            i+=1
        level={n}  # 每一层的数字
        count=0  # 用来记录层数
        while level:
            tmp=set()  # 临时存放每一层的数字
            count+=1
            for l in level:
                for s in square:
                    if s==l:
                        return count
                    if s>l:
                        break
                    tmp.add(l-s)
            level=tmp  # 更新
# Runtime: 240 ms, faster than 76.47% of Python3 online submissions for Perfect Squares.
# Memory Usage: 13.9 MB, less than 19.01% of Python3 online submissions for Perfect Squares.

# 动态规划
class Solution:
    dp = [0]

    def numSquares(self, n: int) -> int:
        while len(self.dp) <= n:
            self.dp += [min(self.dp[-i * i] for i in
                            range(1, int(len(self.dp) ** 0.5 + 1))) + 1]
        return self.dp[n]
# Runtime: 96 ms, faster than 94.50% of Python3 online submissions for Perfect Squares.
# Memory Usage: 13.3 MB, less than 64.60% of Python3 online submissions for Perfect Squares.


# 动态规划，慢很多
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0] * (n + 1)
        left = 1
        while left <= n:
            dp[left] = 1 + min(dp[left - i * i] for i in
                               range(1, int(left**0.5) + 1))
            left += 1
        return dp[-1]
# Runtime: 2404 ms, faster than 7.90% of Python3 online submissions for Perfect Squares.
# Memory Usage: 14 MB, less than 60.00% of Python3 online submissions for Perfect Squares.
