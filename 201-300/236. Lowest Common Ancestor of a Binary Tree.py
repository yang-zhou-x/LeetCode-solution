# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        stack=[root]
        parent={root:None}  # 用来记录节点的父节点
        while p not in parent or q not in parent:
            node=stack.pop()
            if node.left:
                parent[node.left]=node
                stack.append(node.left)
            if node.right:
                parent[node.right]=node
                stack.append(node.right)
        
        ance=set()  # 存放p的父节点路径
        while p:
            ance.add(p)
            p=parent[p]
        while q not in ance:  # 在p的父节点中寻找
            q=parent[q]
            
        return q
        
# Runtime: 80 ms, faster than 93.69% of Python3 online submissions for Lowest Common Ancestor of a Binary Tree.
# Memory Usage: 17.2 MB, less than 80.07% of Python3 online submissions for Lowest Common Ancestor of a Binary Tree.
