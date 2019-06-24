'''
Given a binary tree, you need to compute the length of the diameter of the tree. 
The diameter of a binary tree is the length of the longest path between any two nodes in a tree. 
This path may or may not pass through the root.

Example:
Given a binary tree 
          1
         / \
        2   3
       / \     
      4   5    
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note:
The length of path between two nodes is represented by the number of edges between them.
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# python
class Solution(object):
    def __init__(self):
        self.path=1  # 记录节点总数
        
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node):  # 返回单侧最长路径的节点数，含根节点
            if node is None:
                return 0
            left=dfs(node.left)
            right=dfs(node.right)
            self.path=max(self.path,left+right+1)#记录遍历过程中的最大值
            return max(left,right)+1
        dfs(root)
        return self.path-1  # 长度为节点总数-1
# Runtime: 32 ms, faster than 100.00% of Python online submissions for Diameter of Binary Tree.
# Memory Usage: 13.9 MB, less than 27.04% of Python online submissions for Diameter of Binary Tree.

# python3
class Solution:
    def diameterOfBinaryTree(self, root: 'TreeNode') -> 'int':
        path = 1

        def dfs(node):
            if node:
                left = dfs(node.left)
                right = dfs(node.right)
                nonlocal path
                path = max(path, left+right+1)
                return max(left, right)+1
            else:
                return 0
        dfs(root)
        return path-1
# Runtime: 44 ms, faster than 97.99% of Python3 online submissions for Diameter of Binary Tree.
# Memory Usage: 15.5 MB, less than 84.07% of Python3 online submissions for Diameter of Binary Tree.

# python3
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.path = 1

        def dfs(root):
            if root is None:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            self.path = max(self.path, left+right+1)
            return max(left, right)+1
        dfs(root)
        return self.path-1
# Runtime: 36 ms, faster than 100.00% of Python3 online submissions for Diameter of Binary Tree.
# Memory Usage: 15.8 MB, less than 61.33% of Python3 online submissions for Diameter of Binary Tree.
