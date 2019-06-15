'''
Given a binary tree, determine if it is a valid binary search tree (BST).
Assume a BST is defined as follows:
The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

Example 1:
    2
   / \
  1   3
Input: [2,1,3]
Output: true

Example 2:
    5
   / \
  1   4
     / \
    3   6
Input: [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 解法1，递归
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        nums = []

        def dfs(root):  # inorder遍历
            if root:
                dfs(root.left)
                nums.append(root.val)
                dfs(root.right)
        dfs(root)
        for i in range(1, len(nums)):
            if nums[i-1] >= nums[i]:
                return False
        return True
# Runtime: 52 ms, faster than 84.56% of Python3 online submissions for Validate Binary Search Tree.
# Memory Usage: 16.4 MB, less than 9.06% of Python3 online submissions for Validate Binary Search Tree.

# 解法2，迭代，也为inorder思路，但可以提前终止，不遍历整个树
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        stack = []
        small = float('-inf')
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if root.val <= small:
                return False
            small = root.val
            root = root.right
        return True
# Runtime: 44 ms, faster than 98.36% of Python3 online submissions for Validate Binary Search Tree.
# Memory Usage: 15.5 MB, less than 94.70% of Python3 online submissions for Validate Binary Search Tree.
