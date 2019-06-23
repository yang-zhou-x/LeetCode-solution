'''
You are given a binary tree in which each node contains an integer value.
Find the number of paths that sum to a given value.
The path does not need to start or end at the root or a leaf, 
but it must go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

Example:
root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1
Return 3. The paths that sum to 8 are:
1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11
'''

# python2
class Solution(object):
    def __init__(self):
        self.ans=0
        
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        cache={0:1} # 用来储存指定数字的路径数量。0:根结点符合要求时。
        curr=0
        def aux(node,t,curr,cache):  # t:target,也就是pathSum函数中的sum参数
            if not node:
                return
            curr+=node.val  # curr为当前路径的val总和
            self.ans+=cache.get(curr-t,0)  # curr-(curr-t)=t；全路径-旧路径=目标路径
            cache[curr]=cache.get(curr,0)+1
            aux(node.left,t,curr,cache)
            aux(node.right,t,curr,cache)
            cache[curr]-=1  # 移动到不同branch时, curr不再适用, 因此减去1
        aux(root,sum,curr,cache)
        return self.ans
# Runtime: 40 ms, faster than 94.05% of Python online submissions for Path Sum III.
# Memory Usage: 12.1 MB, less than 57.27% of Python online submissions for Path Sum III.

# 另一种写法。python3
class Solution:
    def pathSum(self, root: 'TreeNode', sum: 'int') -> 'int':
        self.res = 0
        cache = {0: 1}  # {路径上结点之和 : 对应的路径数量}
        self.dfs(root, sum, 0, cache)
        return self.res

    def dfs(self, node, target, curr, cache):
        if node is None:
            return
        curr += node.val
        old = curr-target  # 路径
        self.res += cache.get(old, 0)
        cache[curr] = cache.get(curr, 0)+1
        # 注意cache的变量作用域
        self.dfs(node.left, target, curr, cache)
        self.dfs(node.right, target, curr, cache)
        cache[curr] -= 1
# Runtime: 52 ms, faster than 97.78% of Python3 online submissions for Path Sum III.
# Memory Usage: 14.5 MB, less than 60.48% of Python3 online submissions for Path Sum III.
