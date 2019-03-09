# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def is_sym(root1,root2):  # 使用2个root进行比较，而不是比较1个root的左右子树
            if root1 is None and root2 is None:
                return True
            if root1 and root2:
                return root1.val==root2.val and is_sym(root1.left,root2.right) and is_sym(root1.right,root2.left)
            return False
        return is_sym(root,root)
        
# Runtime: 20 ms, faster than 100.00% of Python online submissions for Symmetric Tree.
# Memory Usage: 11.2 MB, less than 6.35% of Python online submissions for Symmetric Tree.
