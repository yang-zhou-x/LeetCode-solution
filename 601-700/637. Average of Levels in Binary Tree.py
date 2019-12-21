'''
Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.

Example 1:
Input:
    3
   / \
  9  20
    /  \
   15   7
Output: [3, 14.5, 11]
Explanation:
The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].

Note:
The range of node's value is in the range of 32-bit signed integer.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        ans = []
        level = [root]
        while level:
            ans.append(sum(node.val for node in level) / len(level))
            pairs = [(node.left, node.right) for node in level]
            level = [node for pair in pairs for node in pair if node]
        return ans
# Runtime: 52 ms, faster than 71.27% of Python3 online submissions for Average of Levels in Binary Tree.
# Memory Usage: 14.9 MB, less than 100.00% of Python3 online submissions for Average of Levels in Binary Tree.
