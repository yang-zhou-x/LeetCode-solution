'''
Given a binary tree, find the length of the longest path where each node in the path has the same value. 
This path may or may not pass through the root.
The length of path between two nodes is represented by the number of edges between them.

Example 1:
Input:
              5
             / \
            4   5
           / \   \
          1   1   5
Output: 2

Example 2:
Input:
              1
             / \
            4   5
           / \   \
          4   4   5
Output: 2

Note: The given binary tree has not more than 10000 nodes. The height of the tree is not more than 1000.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.ans = 0
        
        def dfs(node):
            if node is None:
                return 0
            left_len = dfs(node.left)
            right_len = dfs(node.right)
            left = right = 0
            if node.left and node.left.val == node.val:
                left = left_len + 1
            if node.right and node.right.val == node.val:
                right = right_len + 1
            # including the case: .left.val == .val == .right.val
            if left + right > self.ans:
                self.ans = left + right
            return max(left, right)
        dfs(root)
        return self.ans
# Runtime: 400 ms, faster than 81.43% of Python3 online submissions for Longest Univalue Path.
# Memory Usage: 16 MB, less than 100.00% of Python3 online submissions for Longest Univalue Path.
