'''
Given a n-ary tree, find its maximum depth.
The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
For example, given a 3-ary tree:

We should return its max depth, which is 3.

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
    def maxDepth(self, root: 'Node') -> int:
        if root is None:
            return 0
        depth = 0
        for child in root.children:
            depth = max(depth, self.maxDepth(child))
        return 1 + depth
# Runtime: 672 ms, faster than 23.50% of Python3 online submissions for Maximum Depth of N-ary Tree.
# Memory Usage: 95.4 MB, less than 8.33% of Python3 online submissions for Maximum Depth of N-ary Tree.


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root is None:
            return 0
        elif not root.children:
            return 1
        else:
            depth_children = []
            for child in root.children:
                depth_children.append(self.maxDepth(child))
            return 1 + max(depth_children)
# Runtime: 684 ms, faster than 14.24% of Python3 online submissions for Maximum Depth of N-ary Tree.
# Memory Usage: 95.4 MB, less than 8.33% of Python3 online submissions for Maximum Depth of N-ary Tree.
