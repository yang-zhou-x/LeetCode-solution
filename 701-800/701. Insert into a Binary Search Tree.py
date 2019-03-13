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
