# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        def pre_order(node):
            if node is None:
                return '[]'
            return '['+str(node.val)+pre_order(node.left)+pre_order(node.right)+']'  # 按照preorder的顺序生成字符串
        return pre_order(s).find(pre_order(t))!=-1
        
# Runtime: 60 ms, faster than 97.46% of Python online submissions for Subtree of Another Tree.
# Memory Usage: 12.3 MB, less than 15.66% of Python online submissions for Subtree of Another Tree.
