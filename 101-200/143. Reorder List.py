'''
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…
You may not modify the values in the list's nodes, only nodes itself may be changed.

Example 1:
Given 1->2->3->4, reorder it to 1->4->2->3.

Example 2:
Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return
        # find the middle node
        slow = fast = p = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # 此时的slow为结果链表的最后1个，无论奇数/偶数
        # reverse the second part
        prev = None
        while slow:
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp
        # 拼接
        while prev.next:
            p.next, p = prev, p.next
            prev.next, prev = p, prev.next
        return 
# Runtime: 96 ms, faster than 69.02% of Python3 online submissions for Reorder List.
# Memory Usage: 22.1 MB, less than 10.00% of Python3 online submissions for Reorder List.            
