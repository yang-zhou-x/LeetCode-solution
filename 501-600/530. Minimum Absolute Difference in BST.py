'''
Given a binary search tree with non-negative values, find the minimum absolute difference 
between values of any two nodes.

Example:
Input:
   1
    \
     3
    /
   2
Output:
1
Explanation:
The minimum absolute difference is 1, which is the difference between 2 and 1 (or between 2 and 3).

Note: There are at least two nodes in this BST.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        nums = []
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            nums.append(root.val)
            root = root.right
        mini = nums[1] - nums[0]
        for i in range(1, len(nums) - 1):
            if nums[i+1] - nums[i] < mini:
                mini = nums[i+1] - nums[i]
        return mini
# Runtime: 60 ms, faster than 93.74% of Python3 online submissions for Minimum Absolute Difference in BST.
# Memory Usage: 15.9 MB, less than 33.33% of Python3 online submissions for Minimum Absolute Difference in BST.
