'''
Given a binary tree, return all root-to-leaf paths.
Note: A leaf is a node with no children.

Example:
Input:
   1
 /   \
2     3
 \
  5
Output: ["1->2->5", "1->3"]
Explanation: All root-to-leaf paths are: 1->2->5, 1->3
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        ans = []
        def dfs(node, path, ans):
            if node is None:
                pass
            elif node.left is None and node.right is None:
                ans.append(path + str(node.val))
            else:
                path += str(node.val) + '->'
                dfs(node.left, path, ans)
                dfs(node.right, path, ans)
        dfs(root, '', ans)
        return ans
# Runtime: 40 ms, faster than 64.51% of Python3 online submissions for Binary Tree Paths.
# Memory Usage: 13.8 MB, less than 9.52% of Python3 online submissions for Binary Tree Paths.
