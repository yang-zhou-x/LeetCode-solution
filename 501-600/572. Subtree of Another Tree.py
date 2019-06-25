'''
Given two non-empty binary trees s and t, check whether tree t has exactly the same structure 
and node values with a subtree of s. A subtree of s is a tree consists of a node in s and 
all of this node's descendants. The tree s could also be considered as a subtree of itself.

Example 1:
Given tree s:
     3
    / \
   4   5
  / \
 1   2
Given tree t:
   4 
  / \
 1   2
Return true, because t has the same structure and node values with a subtree of s.

Example 2:
Given tree s:
     3
    / \
   4   5
  / \
 1   2
    /
   0
Given tree t:
   4
  / \
 1   2
Return false.
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# python
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

# python3
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        def pre(node):
            if node is None:
                return '[]'
            return '['+str(node.val)+pre(node.left)+pre(node.right)+']'
        return pre(s).find(pre(t)) != -1
# Runtime: 80 ms, faster than 95.09% of Python3 online submissions for Subtree of Another Tree.
# Memory Usage: 14.5 MB, less than 32.42% of Python3 online submissions for Subtree of Another Tree.
