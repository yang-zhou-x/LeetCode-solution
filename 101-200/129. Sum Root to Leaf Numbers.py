'''
Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.
An example is the root-to-leaf path 1->2->3 which represents the number 123.
Find the total sum of all root-to-leaf numbers.

Note: A leaf is a node with no children.

Example:
Input: [1,2,3]
    1
   / \
  2   3
Output: 25
Explanation:
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.

Example 2:
Input: [4,9,0,5,1]
    4
   / \
  9   0
 / \
5   1
Output: 1026
Explanation:
The root-to-leaf path 4->9->5 represents the number 495.
The root-to-leaf path 4->9->1 represents the number 491.
The root-to-leaf path 4->0 represents the number 40.
Therefore, sum = 495 + 491 + 40 = 1026.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        ans = []
        
        def dfs(node, path):
            if node.left is None and node.right is None:
                ans.append(path * 10 + node.val)
            else:
                if node.left:
                    dfs(node.left, path * 10 + node.val)
                if node.right:
                    dfs(node.right, path * 10 + node.val)
        if root:
            dfs(root, 0)
        return sum(ans) if root else 0
# Runtime: 40 ms, faster than 57.55% of Python3 online submissions for Sum Root to Leaf Numbers.
# Memory Usage: 13.8 MB, less than 5.55% of Python3 online submissions for Sum Root to Leaf Numbers.
