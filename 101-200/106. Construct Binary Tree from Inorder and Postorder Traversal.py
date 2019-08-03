'''
Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.
For example, given
inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
Return the following binary tree:
    3
   / \
  9  20
    /  \
   15   7
'''

# 复杂度较高，额外占用空间较大
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if inorder:
            idx = inorder.index(postorder.pop())
            root = TreeNode(inorder[idx])
            root.right = self.buildTree(inorder[idx + 1:], postorder)
            root.left = self.buildTree(inorder[:idx], postorder)
            return root
# Runtime: 128 ms, faster than 60.69% of Python3 online submissions for Construct Binary Tree from Inorder and Postorder Traversal.
# Memory Usage: 52.2 MB, less than 65.28% of Python3 online submissions for Construct Binary Tree from Inorder and Postorder Traversal.

# 传递索引，没有列表slice操作
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        mapping = {}
        for i, n in enumerate(inorder):
            mapping[n] = i

        def helper(left, right):
            if left > right:
                return None
            root = TreeNode(postorder.pop())
            idx = mapping[root.val]
            root.right = helper(idx + 1, right)
            root.left = helper(left, idx - 1)
            return root
        return helper(0, len(inorder) - 1)
# Runtime: 64 ms, faster than 91.89% of Python3 online submissions for Construct Binary Tree from Inorder and Postorder Traversal.
# Memory Usage: 18.7 MB, less than 67.71% of Python3 online submissions for Construct Binary Tree from Inorder and Postorder Traversal.
