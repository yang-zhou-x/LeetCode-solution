'''
Given a binary tree, return the postorder traversal of its nodes' values.

Example:
Input: [1,null,2,3]
   1
    \
     2
    /
   3
Output: [3,2,1]

Follow up: Recursive solution is trivial, could you do it iteratively?
'''

# recursion
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []

        def post(node):
            if node:
                post(node.left)
                post(node.right)
                ans.append(node.val)
        post(root)
        return ans
# Runtime: 40 ms, faster than 44.93% of Python3 online submissions for Binary Tree Postorder Traversal.
# Memory Usage: 13.8 MB, less than 5.06% of Python3 online submissions for Binary Tree Postorder Traversal.

# iteration
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                # left-right-root ==> root-right-left
                # pre-order, but right first
                ans.append(node.val)
                stack.append(node.left)
                stack.append(node.right)
        return ans[::-1]  # reverse
# Runtime: 28 ms, faster than 98.65% of Python3 online submissions for Binary Tree Postorder Traversal.
# Memory Usage: 13.8 MB, less than 5.06% of Python3 online submissions for Binary Tree Postorder Traversal.
