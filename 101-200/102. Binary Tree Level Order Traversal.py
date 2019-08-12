'''
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ans = []
        if root:
            level = [root]
            while level:
                ans.append([node.val for node in level])
                lrPair = [(node.left, node.right) for node in level]
                level = [node for lr in lrPair for node in lr if node]
        return ans
# Runtime: 40 ms, faster than 96.15% of Python3 online submissions for Binary Tree Level Order Traversal.


# 2019/08/12更新
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        level = [root]
        ans = []
        while level:
            vals = [node.val for node in level]
            ans.append(vals)
            pairs = [(node.left, node.right) for node in level]
            level = [node for pair in pairs for node in pair if node]
        return ans
# Runtime: 40 ms, faster than 80.01% of Python3 online submissions for Binary Tree Level Order Traversal.
# Memory Usage: 14 MB, less than 16.13% of Python3 online submissions for Binary Tree Level Order Traversal.
