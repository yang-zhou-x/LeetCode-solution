# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        if root is None:
            return 0
        
        if root.val<L:
            return self.rangeSumBST(root.right, L, R)
        elif root.val>R:
            return self.rangeSumBST(root.left, L, R)
        else:
            return self.rangeSumBST(root.left, L, R)+root.val+self.rangeSumBST(root.right, L, R)
        
        
# Runtime: 208 ms, faster than 99.81% of Python3 online submissions for Range Sum of BST.
