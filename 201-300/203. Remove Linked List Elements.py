'''
Remove all elements from a linked list of integers that have value val.

Example:
Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        prev = dummy = ListNode(0)
        curr = dummy.next = head
        while curr:
            if curr.val == val:
                curr = curr.next
                prev.next = curr
            else:
                prev = curr
                curr = curr.next
        return dummy.next
# Runtime: 76 ms, faster than 61.55% of Python3 online submissions for Remove Linked List Elements.
# Memory Usage: 16.9 MB, less than 16.07% of Python3 online submissions for Remove Linked List Elements.
