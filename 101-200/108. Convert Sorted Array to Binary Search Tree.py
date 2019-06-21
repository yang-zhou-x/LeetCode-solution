'''
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
For this problem, a height-balanced binary tree is defined as a binary tree 
in which the depth of the two subtrees of every node never differ by more than 1.

Example:
Given the sorted array: [-10,-3,0,5,9],
One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:
      0
     / \
   -3   9
   /   /
 -10  5
 '''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def help(left, right):
            if left <= right:
                mid = (left+right) >> 1
                root = TreeNode(nums[mid])
                root.left = help(left, mid-1)
                root.right = help(mid+1, right)
                return root
            else:
                return None
        return help(0, len(nums)-1)
        
# Runtime: 60 ms, faster than 93.07% of Python3 online submissions for Convert Sorted Array to Binary Search Tree.
# Memory Usage: 15.2 MB, less than 99.44% of Python3 online submissions for Convert Sorted Array to Binary Search Tree.
