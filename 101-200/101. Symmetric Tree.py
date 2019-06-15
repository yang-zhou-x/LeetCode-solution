'''
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
    1
   / \
  2   2
 / \ / \
3  4 4  3

But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3
   
Note:
Bonus points if you could solve it both recursively and iteratively.
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def nodeSymmetric(node1, node2):  # 使用2个root进行比较，而不是比较1个root的左右子树
            if node1 is None and node2 is None:
                return True
            if node1 and node2:
                if node1.val == node2.val:
                    return nodeSymmetric(node1.left, node2.right) and \
                        nodeSymmetric(node1.right, node2.left)
                else:
                    return False
            else:
                return False
        return nodeSymmetric(root, root)
# Runtime: 32 ms, faster than 98.55% of Python3 online submissions for Symmetric Tree.
# Memory Usage: 13 MB, less than 89.45% of Python3 online submissions for Symmetric Tree.

# 上述解法的简化版
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def is_sym(root1, root2):
            if root1 is None and root2 is None:
                return True
            if root1 and root2:
                return root1.val == root2.val and \
                    is_sym(root1.left, root2.right) and \
                    is_sym(root1.right, root2.left)
            return False
        return is_sym(root, root)
# Runtime: 20 ms, faster than 100.00% of Python online submissions for Symmetric Tree.
# Memory Usage: 11.2 MB, less than 6.35% of Python online submissions for Symmetric Tree.
