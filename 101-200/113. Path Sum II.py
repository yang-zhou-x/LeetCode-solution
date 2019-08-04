'''
Given a binary tree and a sum, 
find all root-to-leaf paths where each path's sum equals the given sum.

Note: A leaf is a node with no children.

Example:
Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
Return:
[
   [5,4,11,2],
   [5,8,4,5]
]
'''

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        ans = []
        def dfs(node, path, tot):
            if node is None:
                return
            if node.left is None and node.right is None and node.val == tot:
                ans.append(path + [node.val])
            else:
                tot -= node.val
                dfs(node.left, path + [node.val], tot)
                dfs(node.right, path + [node.val], tot)
        dfs(root, [], sum)
        return ans
# Runtime: 52 ms, faster than 86.34% of Python3 online submissions for Path Sum II.
# Memory Usage: 19.2 MB, less than 10.07% of Python3 online submissions for Path Sum II.
