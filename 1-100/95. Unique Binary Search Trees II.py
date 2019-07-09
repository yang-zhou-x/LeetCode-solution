'''
Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1 ... n.

Example:
Input: 3
Output:
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
Explanation:
The above output corresponds to the 5 unique BST's shown below:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
'''

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0:
            return []  # 避免返回'[[]]'

        def gen(left, right):
            trees = []
            for val in range(left, right + 1):
                for left_node in gen(left, val - 1):  # 左子树
                    for right_node in gen(val + 1, right):  # 右子树
                        node = TreeNode(val)
                        node.left = left_node
                        node.right = right_node
                        trees.append(node)
            return trees or [None]
        return gen(1, n)
# Runtime: 68 ms, faster than 37.88% of Python3 online submissions for Unique Binary Search Trees II.
# Memory Usage: 15 MB, less than 48.45% of Python3 online submissions for Unique Binary Search Trees II.
