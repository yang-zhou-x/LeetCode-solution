# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.path=1
        
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node):  # 返回树的高度（即：单侧最长）
            if node is None:
                return 0
            left=dfs(node.left)
            right=dfs(node.right)
            self.path=max(self.path,left+right+1)
            return max(left,right)+1
        dfs(root)
        return self.path-1
            
            
# Runtime: 32 ms, faster than 100.00% of Python online submissions for Diameter of Binary Tree.
# Memory Usage: 13.9 MB, less than 27.04% of Python online submissions for Diameter of Binary Tree.
