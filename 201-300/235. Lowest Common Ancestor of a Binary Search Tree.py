'''
Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.
According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between 
two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow 
a node to be a descendant of itself).”
Given binary search tree:  root = [6,2,8,0,4,7,9,null,null,3,5]

Example 1:
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.

Example 2:
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself 
according to the LCA definition.
 
Note:
All of the nodes' values will be unique.
p and q are different and both values will exist in the BST.
'''

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        parents = {root:None}
        stack = [root]
        while p not in parents or q not in parents:
            node = stack.pop()
            if node.left:
                parents[node.left] = node
                stack.append(node.left)
            if node.right:
                parents[node.right] = node
                stack.append(node.right)
        p_parents = {}
        while p:
            p_parents[p] = parents[p]
            p = parents[p]
        while q not in p_parents:
            q = parents[q]
        return q
# Runtime: 100 ms, faster than 20.27% of Python3 online submissions for Lowest Common Ancestor of a Binary Search Tree.
# Memory Usage: 18.1 MB, less than 5.55% of Python3 online submissions for Lowest Common Ancestor of a Binary Search Tree.

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p_val = p.val
        q_val = q.val
        node = root
        while node:
            if p_val > node.val and q_val > node.val:
                node = node.right
            elif p_val < node.val and q_val < node.val:
                node = node.left
            else:
                return node
# Runtime: 84 ms, faster than 87.57% of Python3 online submissions for Lowest Common Ancestor of a Binary Search Tree.
# Memory Usage: 17.9 MB, less than 5.55% of Python3 online submissions for Lowest Common Ancestor of a Binary Search Tree.
