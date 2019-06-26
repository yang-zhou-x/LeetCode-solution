'''
Given a Binary Search Tree and a target number, return true if there exist two elements in the BST 
such that their sum is equal to the given target.

Example 1:
Input: 
    5
   / \
  3   6
 / \   \
2   4   7
Target = 9
Output: True
 
Example 2:
Input: 
    5
   / \
  3   6
 / \   \
2   4   7
Target = 28
Output: False
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        if not root:
            return False
        stack=[root]
        aux=set()
        while stack:
            node=stack.pop()
            if k-node.val in aux:
                return True
            aux.add(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return False
        
# python3
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        if not root:
            return False
        stack = [root]
        cache = set()
        while stack:
            node = stack.pop()
            if k-node.val in cache:
                return True
            cache.add(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return False
# Runtime: 84 ms, faster than 85.52% of Python3 online submissions for Two Sum IV - Input is a BST.
# Memory Usage: 15.7 MB, less than 27.09% of Python3 online submissions for Two Sum IV - Input is a BST.
