'''
Given a binary tree, determine if it is height-balanced.
For this problem, a height-balanced binary tree is defined as:
a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example 1:
Given the following tree [3,9,20,null,null,15,7]:
    3
   / \
  9  20
    /  \
   15   7
Return true.

Example 2:
Given the following tree [1,2,2,3,3,null,null,4,4]:
       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
Return false.
'''

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        self.flag = True

        def get_h(node):
            if not node:
                return 0
            left = get_h(node.left)
            right = get_h(node.right)
            if abs(left - right) > 1:
                self.flag = False
            return 1 + max(left, right)
        get_h(root)
        return self.flag
# Runtime: 56 ms, faster than 85.46% of Python3 online submissions for Balanced Binary Tree.
# Memory Usage: 19.6 MB, less than 5.45% of Python3 online submissions for Balanced Binary Tree.
