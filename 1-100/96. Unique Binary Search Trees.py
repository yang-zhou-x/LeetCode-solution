'''
Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

Example:
Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
'''

'''
输入n时，
1作为根节点的数量: F(0) * F(n-1)
2作为根节点的数量: F(1) * F(n-2) 
3作为根节点的数量: F(2) * F(n-3)
...
n作为根节点的数量: F(n-1) * F(0)
得到公式:
F(n) = F(0) * F(n-1) + F(1) * F(n-2) + F(2) * F(n-3) + ... + F(n-2) * F(1) + F(n-1) * F(0)
'''
class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0]*(n+1)
        dp[0] = 1
        for i in range(1, n+1):
            for j in range(i):
                dp[i] += dp[j]*dp[i-j-1]
        return dp[n]
# Runtime: 36 ms, faster than 82.41% of Python3 online submissions for Unique Binary Search Trees.
# Memory Usage: 13.2 MB, less than 38.27% of Python3 online submissions for Unique Binary Search Trees.
