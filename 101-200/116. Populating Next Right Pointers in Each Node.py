"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root and root.left:  # 同一父节点下的左节点指向右节点
            root.left.next=root.right
            if root.next and root.next.left:  # 不同父节点下的右节点指向左节点
                root.right.next=root.next.left
            self.connect(root.left)  # 递归
            self.connect(root.right)
        return root
        
# Runtime: 56 ms, faster than 84.11% of Python3 online submissions for Populating Next Right Pointers in Each Node.
# Memory Usage: 15 MB, less than 5.48% of Python3 online submissions for Populating Next Right Pointers in Each Node.
