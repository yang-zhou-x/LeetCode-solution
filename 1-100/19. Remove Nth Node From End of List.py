'''
Given a linked list, remove the n-th node from the end of list and return its head.

Example:
Given linked list: 1->2->3->4->5, and n = 2.
After removing the second node from the end, the linked list becomes 1->2->3->5.

Note:
Given n will always be valid.

Follow up:
Could you do this in one pass?
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        p=head
        count=0
        while p:
            count+=1
            p=p.next
        if count<2:
            return None
        if count==n:
            return head.next
        p=head
        for i in range(count-n-1): # 到达被删节点的前一个节点
            p=p.next
        p.next=p.next.next
        return head
# Runtime: 36 ms, faster than 93.59% of Python3 online submissions for Remove Nth Node From End of List.
# Memory Usage: 13.2 MB, less than 45.19% of Python3 online submissions for Remove Nth Node From End of List.
