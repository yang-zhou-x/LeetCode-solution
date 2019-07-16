'''
Given two binary trees, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

Example 1:
Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]
Output: true

Example 2:
Input:     1         1
          /           \
         2             2

        [1,2],     [1,null,2]
Output: false

Example 3:
Input:     1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]
Output: false
'''

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:  # 都为None时
            return True
        if p and q:  # 都非None时
            if p.val != q.val:
                return False
            else:
                return self.isSameTree(p.left, q.left) and \
                    self.isSameTree(p.right, q.right)
        else:  # None和非None
            return False
# Runtime: 24 ms, faster than 99.63% of Python3 online submissions for Same Tree.
# Memory Usage: 13.1 MB, less than 81.70% of Python3 online submissions for Same Tree.
