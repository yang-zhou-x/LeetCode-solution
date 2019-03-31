"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        dic = collections.defaultdict(lambda: Node(0,0,0))
        dic[None] = None
        p = head
        while p:
            dic[p].val = p.val
            dic[p].next = dic[p.next]
            dic[p].random = dic[p.random]
            p = p.next
        return dic[head]
        
# Runtime: 48 ms, faster than 100.00% of Python3 online submissions for Copy List with Random Pointer.
# Memory Usage: 15.5 MB, less than 100.00% of Python3 online submissions for Copy List with Random Pointer.
