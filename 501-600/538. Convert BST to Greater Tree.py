'''
Given a Binary Search Tree (BST), convert it to a Greater Tree 
such that every key of the original BST is changed to the original key 
plus sum of all keys greater than the original key in BST.

Example:
Input: The root of a Binary Search Tree like this:
              5
            /   \
           2     13

Output: The root of a Greater Tree like this:
             18
            /   \
          20     13
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# python2
class Solution(object):
    def __init__(self):
        self.curr=0
        
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root:
            self.convertBST(root.right)
            root.val+=self.curr
            self.curr=root.val
            self.convertBST(root.left)
        return root
        
# 另一种写法，思想相同，python3
class Solution:
    def convertBST(self, root: 'TreeNode') -> 'TreeNode':
        total=0
        def dfs(node):
            if node:
                dfs(node.right)
                nonlocal total
                total+=node.val
                node.val=total
                dfs(node.left)
        dfs(root)
        return root
        
# 更新一下
class Solution:
    def __init__(self):
        self.curr = 0

    def convertBST(self, root: TreeNode) -> TreeNode:
        if root:
            self.convertBST(root.right)
            root.val += self.curr
            self.curr = root.val
            self.convertBST(root.left)
        return root
# Runtime: 76 ms, faster than 94.03% of Python3 online submissions for Convert BST to Greater Tree.
# Memory Usage: 15.6 MB, less than 83.45% of Python3 online submissions for Convert BST to Greater Tree.
