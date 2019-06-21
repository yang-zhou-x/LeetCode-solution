'''
You are given a perfect binary tree where all leaves are on the same level, 
and every parent has two children. The binary tree has the following definition:

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}

Populate each next pointer to point to its next right node. 
If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.
'''

'''
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
'''
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root and root.left:  # 同一父节点下的左节点指向右节点
            root.left.next = root.right
            if root.next and root.next.left:  # 不同父节点下的右节点指向左节点
                root.right.next = root.next.left
            self.connect(root.left)  # 递归
            self.connect(root.right)
        return root
# Runtime: 48 ms, faster than 95.99% of Python3 online submissions for Populating Next Right Pointers in Each Node.
# Memory Usage: 15.3 MB, less than 60.35% of Python3 online submissions for Populating Next Right Pointers in Each Node.
