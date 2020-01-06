'''
Given a binary tree, each node has value 0 or 1.  
Each root-to-leaf path represents a binary number starting with the most significant bit.  
For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent 01101 in binary, which is 13.

For all leaves in the tree, consider the numbers represented by the path from the root to that leaf.
Return the sum of these numbers.

Example 1:
Input: [1,0,1,0,1,0,1]
Output: 22
Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22

Note:
The number of nodes in the tree is between 1 and 1000.
node.val is 0 or 1.
The answer will not exceed 2^31 - 1.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        paths = []
        
        def back_track(node, path):
            if node.left is None and node.right is None:
                paths.append(path + str(node.val))
            else:
                if node.left:
                    back_track(node.left, path + str(node.val))
                if node.right:
                    back_track(node.right, path + str(node.val))
        back_track(root, '')
        return sum(int(x, 2) for x in paths)
# Runtime: 32 ms, faster than 87.30% of Python3 online submissions for Sum of Root To Leaf Binary Numbers.
# Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Sum of Root To Leaf Binary Numbers.
