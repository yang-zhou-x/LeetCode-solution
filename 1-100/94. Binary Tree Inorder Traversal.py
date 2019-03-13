# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res=[]
        self._aux(root,res)
        
        return res
        
    def _aux(self,root,res):
        if root:
            self._aux(root.left,res)
            res.append(root.val)
            self._aux(root.right,res)
            
# Runtime: 32 ms, faster than 99.77% of Python3 online submissions for Binary Tree Inorder Traversal.
