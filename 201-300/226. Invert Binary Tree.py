# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root:
            tmp=root.left
            root.left=root.right
            root.right=tmp
            self.invertTree(root.left)
            self.invertTree(root.right)
        return root
            
# Runtime: 16 ms, faster than 100.00% of Python online submissions for Invert Binary Tree.
# Memory Usage: 10.7 MB, less than 77.97% of Python online submissions for Invert Binary Tree.
