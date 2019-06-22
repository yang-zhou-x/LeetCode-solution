'''
Invert a binary tree.

Example:
Input:
     4
   /   \
  2     7
 / \   / \
1   3 6   9
Output:
     4
   /   \
  7     2
 / \   / \
9   6 3   1

Trivia:
This problem was inspired by this original tweet by Max Howell:
Google: 90% of our engineers use the software you wrote (Homebrew), 
but you can’t invert a binary tree on a whiteboard so f*** off.
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# python2
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root:
            tmp = root.left
            root.left = root.right
            root.right = tmp
            self.invertTree(root.left)
            self.invertTree(root.right)
        return root
# Runtime: 16 ms, faster than 100.00% of Python online submissions for Invert Binary Tree.
# Memory Usage: 10.7 MB, less than 77.97% of Python online submissions for Invert Binary Tree.

# python3
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root:
            tmp = root.left
            root.left = self.invertTree(root.right)
            root.right = self.invertTree(tmp)
        return root
# Runtime: 32 ms, faster than 92.60% of Python3 online submissions for Invert Binary Tree.
# Memory Usage: 13.1 MB, less than 80.98% of Python3 online submissions for Invert Binary Tree.
