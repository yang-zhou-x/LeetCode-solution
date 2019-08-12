'''
Given a binary tree, return the bottom-up level order traversal of its nodes' values. 
(ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:

[
  [15,7],
  [9,20],
  [3]
]
'''

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        ans = []
        level = [root]
        while level:
            vals = [node.val for node in level]
            ans.append(vals)
            pairs = [(node.left, node.right) for node in level]
            level = [node for pair in pairs for node in pair if node]
        ans.reverse()
        return ans
# Runtime: 44 ms, faster than 50.94% of Python3 online submissions for Binary Tree Level Order Traversal II.
