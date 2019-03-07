# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.curr=0
        
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root:
            self.convertBST(root.right)
            root.val+=self.curr
            self.curr=root.val
            self.convertBST(root.left)
        return root
        
# 另一种方法，思想相同，python3
class Solution:
    def convertBST(self, root: 'TreeNode') -> 'TreeNode':
        total=0
        def dfs(node):
            if node:
                dfs(node.right)
                nonlocal total
                total+=node.val
                node.val=total
                dfs(node.left)
        dfs(root)
        return root
        
