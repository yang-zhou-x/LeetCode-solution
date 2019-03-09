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
