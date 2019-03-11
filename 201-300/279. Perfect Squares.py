class Solution:
    def numSquares(self, n: int) -> int:
        # BFS算法
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
