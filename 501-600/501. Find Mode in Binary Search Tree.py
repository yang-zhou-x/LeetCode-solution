'''
Given a binary search tree (BST) with duplicates, find all the mode(s) (the most frequently occurred element) 
in the given BST.

Assume a BST is defined as follows:
The left subtree of a node contains only nodes with keys less than or equal to the node's key.
The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
Both the left and right subtrees must also be binary search trees.

For example:
Given BST [1,null,2,2],
   1
    \
     2
    /
   2
return [2].

Note: If a tree has more than one mode, you can return them in any order.
Follow up: Could you do that without using any extra space? (Assume that the 
implicit stack space incurred due to recursion does not count).
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import Counter

class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        nums = []
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            nums.append(root.val)
            root = root.right
        nums = Counter(nums)
        # maxi_key = sorted(nums, key=d.get, reverse=True)[0]
        maxi_cnt = sorted(nums.values())[-1]
        ans = []
        for key in nums:
            if nums[key] == maxi_cnt:
                ans.append(key)
        return ans
# Runtime: 64 ms, faster than 78.46% of Python3 online submissions for Find Mode in Binary Search Tree.
# Memory Usage: 18 MB, less than 8.33% of Python3 online submissions for Find Mode in Binary Search Tree.
