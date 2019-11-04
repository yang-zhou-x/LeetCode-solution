'''
Given a binary tree, return the tilt of the whole tree.
The tilt of a tree node is defined as the absolute difference between the sum of all 
left subtree node values and the sum of all right subtree node values. Null node has tilt 0.
The tilt of the whole tree is defined as the sum of all nodes' tilt.

Example:
Input: 
         1
       /   \
      2     3
Output: 1
Explanation: 
Tilt of node 2 : 0
Tilt of node 3 : 0
Tilt of node 1 : |2-3| = 1
Tilt of binary tree : 0 + 0 + 1 = 1

Note:
The sum of node values in any subtree won't exceed the range of 32-bit integer.
All the tilt values won't exceed the range of 32-bit integer.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTilt(self, root: TreeNode) -> int:
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 0
        left_tilt = self.findTilt(root.left)
        right_tilt = self.findTilt(root.right)
        curr_left = root.left.val if root.left else 0
        curr_right = root.right.val if root.right else 0
        curr_tilt = abs(curr_left - curr_right)
        return left_tilt + right_tilt + curr_tilt
# input为[1,2,3,4,null,5]时出错。
# 实际输出为10，期望输出为11。题意有些confusion，我手算了一下也是10。


# 另一种理解题意的方式
class Solution:
    def findTilt(self, root: TreeNode) -> int:
        self.ans = 0
        
        def dfs(root):
            if root is None:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            self.ans += abs(left - right)
            return left + right + root.val
        dfs(root)
        return self.ans
# Runtime: 68 ms, faster than 65.28% of Python3 online submissions for Binary Tree Tilt.
# Memory Usage: 16.6 MB, less than 8.33% of Python3 online submissions for Binary Tree Tilt.
