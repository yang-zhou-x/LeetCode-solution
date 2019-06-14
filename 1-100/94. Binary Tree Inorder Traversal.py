'''
Given a binary tree, return the inorder traversal of its nodes' values.

Follow up: 
Recursive solution is trivial, could you do it iteratively?
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        nums = []

        def dfs(root):
            if root:
                dfs(root.left)
                nums.append(root.val)
                dfs(root.right)
        dfs(root)
        return nums
# Runtime: 32 ms, faster than 94.21% of Python3 online submissions for Binary Tree Inorder Traversal.
# Memory Usage: 13.2 MB, less than 28.91% of Python3 online submissions for Binary Tree Inorder Traversal.
