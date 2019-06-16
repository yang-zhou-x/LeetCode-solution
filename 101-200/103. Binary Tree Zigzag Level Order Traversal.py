'''
Given a binary tree, return the zigzag level order traversal of its nodes' values. 
(ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
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
    def zigzagLevelOrder(self, root: 'TreeNode') -> 'List[List[int]]':
        if not root:
            return []
        level = [root]
        ans = []
        fromRight = False
        while level:
            vals = [node.val for node in level]
            if fromRight:
                vals.reverse()
            ans.append(vals)
            fromRight = not fromRight
            lrPairs = [(node.left, node.right) for node in level]
            level = [node for lr in lrPairs for node in lr if node]
        return ans
# Runtime: 36 ms, faster than 99.52% of Python3 online submissions for Binary Tree Zigzag Level Order Traversal.

# 2019/6/16更新，没啥区别
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        ans = []
        fromRight = False
        level = [root]
        while level:
            val = [node.val for node in level]
            if fromRight:
                val.reverse()
            ans.append(val)
            fromRight = not fromRight
            pairs = [(node.left, node.right) for node in level]
            level = [node for pair in pairs for node in pair if node]
        return ans
# Runtime: 32 ms, faster than 98.46% of Python3 online submissions for Binary Tree Zigzag Level Order Traversal.
# Memory Usage: 13.7 MB, less than 5.01% of Python3 online submissions for Binary Tree Zigzag Level Order Traversal.
