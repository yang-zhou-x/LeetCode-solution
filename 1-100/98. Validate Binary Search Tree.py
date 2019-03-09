# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        nums=[]
        def in_order(node):  # inorder顺序输出
            if node:
                in_order(node.left)
                nonlocal nums
                nums.append(node.val)
                in_order(node.right)
        in_order(root)
        for i in range(len(nums)-1):
            if nums[i]>=nums[i+1]:
                return False
        return True

# 简化版本，也为inorder思路：
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        stack=[]
        small=float('-inf')
        while stack or root:
            while root:
                stack.append(root)
                root=root.left
            root=stack.pop()
            if root.val<=small:
                return False
            small=root.val
            root=root.right
        return True
     
         



