'''
Given a binary tree, find its minimum depth.
The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its minimum depth = 2.
'''

class Solution:  # Runtime: 52 ms, faster than 66.09%
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        if root.left is None or root.right is None:
            return 1 + self.minDepth(root.left) + self.minDepth(root.right)
        else:
            return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
            
