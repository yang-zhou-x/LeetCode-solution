'''
A binary tree is univalued if every node in the tree has the same value.
Return true if and only if the given tree is univalued.

Example 1:
Input: [1,1,1,1,1,null,1]
Output: true

Example 2:
Input: [2,2,2,5,2]
Output: false

Note:
The number of nodes in the given tree will be in the range [1, 100].
Each node's value will be an integer in the range [0, 99].
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        val = root.val
        
        def dfs(root):
            if root is None:
                return True
            if root.val == val:
                return dfs(root.left) and dfs(root.right)
            else:
                return False
        return dfs(root)
# Runtime: 20 ms, faster than 98.80% of Python3 online submissions for Univalued Binary Tree.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Univalued Binary Tree.
