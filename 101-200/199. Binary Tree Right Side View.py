'''
Given a binary tree, imagine yourself standing on the right side of it, 
return the values of the nodes you can see ordered from top to bottom.

Example:
Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:
   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        ans = []
        level = [root]
        while level:
            ans.append(level[-1].val)
            pairs = [(node.left, node.right) for node in level]
            level = [node for pair in pairs for node in pair if node]
        return ans
# Runtime: 36 ms, faster than 82.83% of Python3 online submissions for Binary Tree Right Side View.
# Memory Usage: 13.8 MB, less than 5.26% of Python3 online submissions for Binary Tree Right Side View.
