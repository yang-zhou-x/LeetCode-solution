# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        stack=[]
        inorder=float('-inf')
        while stack or root:
            while root:
                stack.append(root)
                root=root.left
            root=stack.pop()
            if root.val<=inorder:
                return False
            inorder=root.val
            root=root.right
        return True


# another way, also in-order
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        nums=[]
        def in_order(node):
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
