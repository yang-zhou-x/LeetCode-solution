'''
Given an n-ary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
For example, given a 3-ary tree:

We should return its level order traversal:
[
     [1],
     [3,2,4],
     [5,6]
]
 
Note:
The depth of the tree is at most 1000.
The total number of nodes is at most 5000.
'''

"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        ans = []
        if not root:
            return ans
        level = [root]
        while level:
            level_vals = [node.val for node in level]
            ans.append(level_vals)
            level = [child for node in level for child in node.children if child]
        return ans
# Runtime: 660 ms, faster than 80.40% of Python3 online submissions for N-ary Tree Level Order Traversal.
# Memory Usage: 95 MB, less than 8.33% of Python3 online submissions for N-ary Tree Level Order Traversal.
