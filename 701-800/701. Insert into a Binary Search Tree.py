'''
Given the root node of a binary search tree (BST) and a value to be inserted into the tree, 
insert the value into the BST. Return the root node of the BST after the insertion. 
It is guaranteed that the new value does not exist in the original BST.

Note that there may exist multiple valid ways for the insertion, 
as long as the tree remains a BST after insertion. You can return any of them.

For example, 
Given the tree:
        4
       / \
      2   7
     / \
    1   3
And the value to insert: 5
You can return this binary search tree:

         4
       /   \
      2     7
     / \   /
    1   3 5
This tree is also valid:

         5
       /   \
      2     7
     / \   
    1   3
         \
          4
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if root is None:
            root=TreeNode(val)
        elif val<root.val:
            root.left=self.insertIntoBST(root.left,val)
        else:
            root.right=self.insertIntoBST(root.right,val)
        return root
# Runtime: 124 ms, faster than 69.08% of Python3 online submissions for Insert into a Binary Search Tree.
# Memory Usage: 15.1 MB, less than 5.32% of Python3 online submissions for Insert into a Binary Search Tree.

# python3
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if root is None:
            return TreeNode(val)
        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)
        return root
# Runtime: 124 ms, faster than 69.94% of Python3 online submissions for Insert into a Binary Search Tree.
# Memory Usage: 15.4 MB, less than 39.78% of Python3 online submissions for Insert into a Binary Search Tree.
