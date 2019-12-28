'''
Consider all the leaves of a binary tree.  From left to right order, 
the values of those leaves form a leaf value sequence.

For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).
Two binary trees are considered leaf-similar if their leaf value sequence is the same.
Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

Note:
Both of the given trees will have between 1 and 100 nodes.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        nums = []
        
        def dfs(root):
            if not root:
                pass
            elif not root.left and not root.right:
                nums.append(root.val)
            else:
                dfs(root.left)
                dfs(root.right)
        dfs(root1)
        nums.append('anchor')
        dfs(root2)
        anchor = nums.index('anchor')
        if anchor != len(nums) - 1 - anchor:
            return False
        return nums[:anchor] == nums[anchor+1:]
# Runtime: 20 ms, faster than 99.79% of Python3 online submissions for Leaf-Similar Trees.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Leaf-Similar Trees.
