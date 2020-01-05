'''
In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.
Two nodes of a binary tree are cousins if they have the same depth, but have different parents.
We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.
Return true if and only if the nodes corresponding to the values x and y are cousins.

Example 1:
Input: root = [1,2,3,4], x = 4, y = 3
Output: false

Example 2:
Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
Output: true

Example 3:
Input: root = [1,2,3,null,4], x = 2, y = 3
Output: false

Note:
The number of nodes in the tree will be between 2 and 100.
Each node has a unique integer value from 1 to 100.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        self.ans = {}
        self.found = 0
        
        def back_track(node, depth, parent_val):
            if node is None:
                return None
            if node.val in (x, y):
                self.ans[node.val] = (depth, parent_val)
                self.found += 1
                if self.found == 2:
                    return None
            back_track(node.left, depth + 1, node.val)
            back_track(node.right, depth + 1, node.val)
        
        back_track(root, 0, None)
        if self.ans[x][0] == self.ans[y][0] and self.ans[x][1] != self.ans[y][1]:
            return True
        else:
            return False
# Runtime: 28 ms, faster than 81.14% of Python3 online submissions for Cousins in Binary Tree.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Cousins in Binary Tree.
