'''
Given a binary tree, flatten it to a linked list in-place.
For example, given the following tree:
    1
   / \
  2   5
 / \   \
3   4   6
The flattened tree should look like:
1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        prev = TreeNode(0)
        stack = [root]
        while stack:
            node = stack.pop()
            prev.right = node
            prev.left = None
            if node and node.right:
                stack.append(node.right)
            if node and node.left:
                stack.append(node.left)
            prev = node
# Runtime: 44 ms, faster than 59.39% of Python3 online submissions for Flatten Binary Tree to Linked List.
# Memory Usage: 13.8 MB, less than 8.70% of Python3 online submissions for Flatten Binary Tree to Linked List.
