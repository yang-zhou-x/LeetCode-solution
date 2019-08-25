'''
Given a binary tree, return the preorder traversal of its nodes' values.

Example:
Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,2,3]
Follow up: Recursive solution is trivial, could you do it iteratively?
'''

# recursion
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        ans =[]
        
        def pre(node):
            if node:
                ans.append(node.val)
                pre(node.left)
                pre(node.right)
        pre(root)
        return ans
# Runtime: 32 ms, faster than 92.62% of Python3 online submissions for Binary Tree Preorder Traversal.
# Memory Usage: 14 MB, less than 5.24% of Python3 online submissions for Binary Tree Preorder Traversal.

# iteration
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                ans.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return ans
# Runtime: 28 ms, faster than 99.25% of Python3 online submissions for Binary Tree Preorder Traversal.
# Memory Usage: 13.9 MB, less than 6.52% of Python3 online submissions for Binary Tree Preorder Traversal.
