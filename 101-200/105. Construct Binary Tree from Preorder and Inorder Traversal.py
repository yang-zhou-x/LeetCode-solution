'''
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 递归方法
class Solution:
    def buildTree(self, preorder: 'List[int]', inorder: 'List[int]') -> 'TreeNode':
        if inorder:
            idx = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[idx])
            root.left = self.buildTree(preorder, inorder[:idx])
            root.right = self.buildTree(preorder, inorder[idx+1:])
            return root
# Runtime: 140 ms, faster than 75.10% of Python3 online submissions for Construct Binary Tree from Preorder and Inorder Traversal.
# Memory Usage: 52.4 MB, less than 47.37% of Python3 online submissions for Construct Binary Tree from Preorder and Inorder Traversal.


# 传递索引，避免列表slice操作
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        mapping = {n: i for i, n in enumerate(inorder)}

        def build(left, right):
            if left > right:
                return None
            root = TreeNode(preorder.pop(0))
            idx = mapping[root.val]
            root.left = build(left, idx - 1)
            root.right = build(idx + 1, right)
            return root
        return build(0, len(inorder) - 1)
# Runtime: 68 ms, faster than 82.49% of Python3 online submissions for Construct Binary Tree from Preorder and Inorder Traversal.
# Memory Usage: 18.6 MB, less than 71.05% of Python3 online submissions for Construct Binary Tree from Preorder and Inorder Traversal.


# 迭代方法，更快
class Solution:
    def buildTree(self, preorder: 'List[int]', inorder: 'List[int]') -> 'TreeNode':
        if not preorder:
            return
        pre_iter, in_iter = iter(preorder), iter(inorder)
        root = TreeNode(next(pre_iter))
        curr_in_val = next(in_iter)

        stack = [root]
        node = root
        build_right = False

        while True:
            try:
                if stack and stack[-1].val == curr_in_val:
                    node = stack.pop()
                    curr_in_val = next(in_iter)
                    build_right = True
                else:
                    if build_right:
                        node.right = TreeNode(next(pre_iter))
                        node = node.right
                        build_right = False
                    else:
                        node.left = TreeNode(next(pre_iter))
                        node = node.left
                    stack.append(node)
            except StopIteration:
                break
        return root
# Runtime: 48 ms, faster than 99.93% of Python3 online submissions for Construct Binary Tree from Preorder and Inorder Traversal. 
