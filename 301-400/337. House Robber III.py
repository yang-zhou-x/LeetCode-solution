'''
The thief has found himself a new place for his thievery again. 
There is only one entrance to this area, called the "root." 
Besides the root, each house has one and only one parent house. 
After a tour, the smart thief realized that "all houses in this place forms a binary tree". 
It will automatically contact the police if two directly-linked houses were broken into on the same night.

Determine the maximum amount of money the thief can rob tonight without alerting the police.

Example 1:
Input: [3,2,3,null,3,null,1]
     3
    / \
   2   3
    \   \ 
     3   1
Output: 7 
Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.

Example 2:
Input: [3,4,5,1,3,null,1]
     3
    / \
   4   5
  / \   \ 
 1   3   1
Output: 9
Explanation: Maximum amount of money the thief can rob = 4 + 5 = 9.
'''

class Solution:
    def rob(self, root: TreeNode) -> int:
        def superrob(node):
            # returns tuple of size two (now, later)
            # now: max money earned if input node is robbed
            # later: max money earned if input node is not robbed
            # base case
            if not node: 
                return (0, 0)
            # get values
            left, right = superrob(node.left), superrob(node.right)
            # rob now
            now = node.val + left[1] + right[1]
            # rob later
            later = max(left) + max(right)
            return (now, later)
        return max(superrob(root))
# Runtime: 52 ms, faster than 92.86% of Python3 online submissions for House Robber III.
# Memory Usage: 16 MB, less than 32.86% of Python3 online submissions for House Robber III.
